from abc import abstractmethod
import random

from ..base import AbstractEngine
from .realms import Realm

class AbstractParamsEngine(AbstractEngine):
    TIMING = ['run']
    CLI_PREFIX = "--"
    CLI_GLUE = "="
    CLI_BOOLEAN = 'show' # show ; hide ; prefix
    CLI_BOOLEAN_PREFIX_TRUE = ''
    CLI_BOOLEAN_PREFIX_FALSE = 'no-'
    SILENT_PREFIX = '@'
    SILENT_SUFFIX = '$'

    def __init__(self):
        self.config = {
            'timing': self.TIMING,
            'cli_prefix': self.CLI_PREFIX,
            'cli_glue': self.CLI_GLUE,
            'cli_boolean': self.CLI_BOOLEAN,
            'cli_boolean_prefix_true': self.CLI_BOOLEAN_PREFIX_TRUE,
            'cli_boolean_prefix_false': self.CLI_BOOLEAN_PREFIX_FALSE,
            'silent_prefix': self.SILENT_PREFIX,
            'silent_suffix': self.SILENT_SUFFIX,
        }

    @abstractmethod
    def get_contents(self, file_path):
        pass

    def get_locations(self, file_contents):
        return {'param': list(file_contents['current'].keys())}

    def location_names(self, locations, target_file, target_type):
        return locations[target_file][target_type]

    def dump(self, file_contents):
        return "\n".join(['{} := {}'.format(k, repr(v)) for k,v in file_contents['current'].items() if not self.would_be_ignored(file_contents, k, v)])

    def show_location(self, contents, locations, target_file, target_type, target_loc):
        if target_type != 'param':
            return '(unsupported)'
        params = contents[target_file]['current']
        space = contents[target_file]['space']
        return '{}: {} default={}'.format(target_loc, str(space[target_loc]), repr(params[target_loc]))

    def random_target(self, locations, weights, target_file, target_type=None):
        if target_type is None:
            target_type = random.choice(locations[target_file])
        if weights and target_file in weights and target_type in weights[target_file]:
            total_weight = sum(weights[target_file][target_type].values())
            r = random.uniform(0, total_weight)
            for loc, w in weights[target_file][target_type].items():
                if r < w:
                    return (target_file, target_type, loc)
                r -= w
            return None
        else:
            try:
                loc = random.choice(locations[target_file][target_type])
                return (target_file, target_type, loc)
            except (KeyError, ValueError):
                return None

    def resolve_cli(self, file_contents):
        params = file_contents['current']
        # original
        # return ' '.join([s for s in [self.resolve_cli_param(params, k, v) for k,v in params.items() if not self.would_be_ignored(file_contents, k, v)] if s != ''])
        
        temp = list()
        cli = ""
        for k,v in params.items():
            if not self.would_be_ignored(file_contents, k, v):
                temp.append(self.resolve_cli_param(params, k, v))
        for s in temp:
            if s != "":
                cli = '{} {}'.format(cli, s)
        return cli 

    def resolve_cli_param(self, all_params, param, value):
        if param.startswith(self.config['silent_prefix']):
            return ''
        if self.config['silent_suffix'] in param:
            cli_param, *_ = param.split(self.silent_suffix)
        else:
            cli_param = param
        if str(value) == 'True':
            if self.config['cli_boolean'] == 'hide':
                return '{}{}'.format(self.config['cli_prefix'], cli_param)
            elif self.config['cli_boolean'] == 'prefix':
                return '{}{}{}'.format(self.config['cli_prefix'], self.config['cli_boolean_prefix_true'], cli_param)
        elif str(value) == 'False':
            if self.config['cli_boolean'] == 'hide':
                return ''
            elif self.config['cli_boolean'] == 'prefix':
                return '{}{}{}'.format(self.config['cli_prefix'], self.config['cli_boolean_prefix_false'], cli_param)
        return '{}{}{}{}'.format(self.config['cli_prefix'], cli_param, self.config['cli_glue'], repr(value))

    def would_be_ignored(self, file_contents, key, value):
        """ For conditional parameters. """
        # original code.
        # return any(file_contents['current'][_k2] not in _vals for (_k1, _k2, _vals) in file_contents['conditionals'] if _k1 == key)
        
        # Add str() to file_contents['current'][_k2] to fix bug.
        results = list()
        for (_k1, _k2, _vals) in file_contents['conditionals']:
            if _k1 == key:
                temp = str(file_contents['current'][_k2]) not in _vals
                results.append(temp)
        return any(results)

    def would_be_valid(self, file_contents, key, value):
        """ For forbidden parameters. """
        for d in file_contents['forbidden']:
            forbidden = True
            for k in d.keys():
                if (k != key and d[k] != file_contents['current'][k]) or (k == key and d[k] != value):
                    forbidden = False
                    break
            if forbidden:
                return False
        return True

    def do_set(self, contents, locations, new_contents, new_locations, target, value):
        file_contents = new_contents[target[0]]
        key = target[1]
        
        # Check for forbidden parameters
        forbidden = False
        for dictionary in file_contents['forbidden']:
            # The key is part of forbidden parameter set and the value matches.
            if key in dictionary and str(value) == str(dictionary[key]):
                # Loop through the forbidden set.
                for f_param, f_value in dictionary.items():
                    # Check for a match between current configuration with the incoming parameter setting.
                    if f_param != key and str(f_value) == str(file_contents['current'][f_param]):
                        # There is a conflict as the incoming parameter match the forbidden value
                        # and there is also a match for other forbidden parameters.
                        forbidden = True
                        break
            if forbidden == True:
                break

        used = self.would_be_valid(file_contents, key, value) and not self.would_be_ignored(file_contents, key, value) and not forbidden
        if used:
            file_contents['current'][key] = value
        return used

    def random_value(self, file_contents, param_key):
        realm = file_contents['space'][param_key]
        return Realm.random_value_from_realm(realm)
