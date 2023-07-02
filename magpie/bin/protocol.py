import io
import os

import magpie

class BasicProtocol:
    def __init__(self):
        self.search = None
        self.program = None

    def setup(self, config):
        # shared parameters
        sec = config['search']
        self.search.config['warmup'] = int(sec['warmup'])
        self.search.config['warmup_strategy'] = sec['warmup_strategy']
        self.search.stop['steps'] = int(val) if (val := sec['max_steps']) else None
        self.search.stop['wall'] = int(val) if (val := sec['max_time']) else None
        self.search.stop['fitness'] = int(val) if (val := sec['target_fitness']) else None
        self.search.config['cache_maxsize'] = int(val) if (val := sec['cache_maxsize']) else 0
        self.search.config['cache_keep'] = float(sec['cache_keep'])

        self.search.config['possible_edits'] = []
        for edit in sec['possible_edits'].split():
            for klass in [*magpie.xml.edits, *magpie.line.edits, *magpie.params.edits]:
                if klass.__name__ == edit:
                    self.search.config['possible_edits'].append(klass)
                    break
            else:
                raise ValueError('Invalid config file: unknown edit type "{}" in "[software] possible_edits"'.format(edit))
        print("possible_edits:", self.search.config['possible_edits'])
        if self.search.config['possible_edits'] == []:
            raise ValueError('Invalid config file: "[search] possible_edits" must be non-empty!')

        # local search only
        if isinstance(self.search, magpie.algo.LocalSearch):
            sec = config['search.ls']
            self.search.config['delete_prob'] = float(sec['delete_prob'])
            self.search.config['max_neighbours'] = int(val) if (val := sec['max_neighbours']) else None
            self.search.config['when_trapped'] = sec['when_trapped']
            self.search.config['accept_fail'] = sec['accept_fail']
            self.search.config['tabu_length'] = sec['tabu_length']

        # genetic programming only
        if isinstance(self.search, magpie.algo.GeneticProgramming):
            sec = config['search.gp']
            self.search.config['pop_size'] = int(sec['pop_size'])
            self.search.config['delete_prob'] = float(sec['delete_prob'])
            self.search.config['offspring_elitism'] = float(sec['offspring_elitism'])
            self.search.config['offspring_crossover'] = float(sec['offspring_crossover'])
            self.search.config['offspring_mutation'] = float(sec['offspring_mutation'])
            self.search.config['uniform_rate'] = float(sec['uniform_rate'])

        # log config just in case
        with io.StringIO() as ss:
            config.write(ss)
            ss.seek(0)
            self.program.logger.debug('==== CONFIG ====\n{}'.format(ss.read()))

    def run(self):
        if self.program is None:
            raise AssertionError('Program not specified')
        if self.search is None:
            raise AssertionError('Search not specified')

        self.search.program = self.program

        # run the algorithm a single time
        logger = self.program.logger
        result = {'stop': None, 'best_patch': []}
        self.search.run()
        result.update(self.search.report)
        logger.info('')

        # print the report
        logger.info('==== REPORT ====')
        logger.info('Termination: {}'.format(result['stop']))
        for handler in logger.handlers:
            if handler.__class__.__name__ == 'FileHandler':
                logger.info('Log file: {}'.format(handler.baseFilename))
        if result['best_patch']:
            result['diff'] = self.program.diff_patch(result['best_patch'])
            base_path = os.path.join(magpie.config.log_dir, self.program.run_label)
            logger.info('Patch file: {}'.format('{}.patch'.format(base_path)))
            logger.info('Diff file: {}'.format('{}.diff'.format(base_path)))
            logger.info('Best fitness: {}'.format(result['best_fitness']))
            logger.info('Best patch: {}'.format(result['best_patch']))
            logger.info('Diff:\n{}'.format(result['diff']))
            # for convenience, save best patch and diff to separate files
            with open('{}.patch'.format(base_path), 'w') as f:
                f.write(str(result['best_patch'])+"\n")
            with open('{}.diff'.format(base_path), 'w') as f:
                f.write(result['diff'])

        # cleanup temporary software copies
        self.program.clean_work_dir()
