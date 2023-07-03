import random
from ..base import Edit
from . import AbstractParamsEngine

class ParamSetting(Edit):
    def apply(self, program, new_contents, new_locations):
        engine = program.engines[self.target[0]]
        return engine.do_set(program.contents, program.locations,
                             new_contents, new_locations,
                             self.target, self.data[0])

    @classmethod
    def create(cls, program, target_file=None):
        if target_file is None:
            target_file = program.random_file(AbstractParamsEngine)
        _, _, param_id = program.random_target(target_file, 'param')
        print('param_id: {}'.format(param_id), 'target_file: {}'.format(target_file))
        engine = program.engines[target_file]
        data = engine.random_value(program.contents[target_file], param_id)
        return cls((target_file, param_id), data)
    
    @classmethod
    def randomly_initialise_population(cls, program, target_file=None):
        if target_file is None:
            target_file = program.random_file(AbstractParamsEngine)

        engine = program.engines[target_file]
        configuration = dict()
        for k, v in program.contents[target_file]['space'].items():
            data = engine.random_value(program.contents[target_file], k)
            configuration[k] = data
        
        return configuration
