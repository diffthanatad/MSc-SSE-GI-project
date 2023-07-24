import copy
import random
import time

from ..base import Algorithm, Patch
from ..params import CategoricalRealm, GeometricRealm, UniformIntRealm

class ParticleSwarmOptimization(Algorithm):
    params = dict()                     # magpie.params.realms
    pop_size = 40
    speed_max = 3
    speed_min = -3
    category_params = dict()            # class CategoricalRealm

    population = list()                 # class Particle
    global_best = None                  # class Particle

    def setup(self):
        super().setup()
        self.name = 'Particle Swarm Optimisation'
         
    def reset(self):
        super().reset()
        self.stats['gen'] = 0

    def aux_log_counter(self):
        return '{}-{}'.format(self.stats['gen'], self.stats['steps']%self.pop_size+1)

    def run(self):
        try:
            # warmup
            self.hook_warmup()
            self.warmup()

            # PSO set up.
            # (1) how many parameters are there?
            target_file = self.find_target_file_param()
            self.params.clear()
            self.params.update(self.program.contents[target_file]['space'])
            # (2) search for categorical params
            for param_id, value in self.program.contents[target_file]['space'].items():
                if isinstance(value, CategoricalRealm):
                    self.category_params[param_id] = value

            self.initialise_population() # initialise population and velocity at the same time

            # start!, 1st generation
            self.hook_start() 
            local_best_fitness = None
            for i, particle in enumerate(self.population):
                if self.stopping_condition():
                    break

                patch = self.create_particle_patch(particle)
                
                run = self.evaluate_patch(patch)
                particle.best_fitness = run.fitness

                if i == 0:
                    self.global_best =  particle
                
                accept = best = False
                if run.status == 'SUCCESS':
                    if self.dominates(run.fitness, local_best_fitness):
                        self.program.logger.debug(self.program.diff_patch(patch))
                        local_best_fitness = run.fitness
                        accept = True
                        if self.dominates(run.fitness, self.report['best_fitness']):
                            self.report['best_fitness'] = run.fitness
                            self.report['best_patch'] = patch
                            best = True
                            self.global_best = particle
                
                self.hook_evaluation(patch, run, accept, best)
                self.stats['steps'] += 1

            # evaluate 2nd - nth generation
            while not self.stopping_condition():
                self.stats['gen'] += 1
                self.hook_main_loop()
                
                local_best_fitness =  None
                for particle in self.population:
                    if self.stopping_condition():
                        break

                    # update speed and position
                    particle.update_speed(self.global_best)
                    particle.update_position(self.params)

                    # evaluate
                    patch = self.create_particle_patch(particle)
                    run = self.evaluate_patch(patch)

                    # update particle best
                    if self.dominates(run.fitness, particle.best_fitness):
                        particle.update_best(run.fitness)
                    
                    accept = best = False
                    if run.status == 'SUCCESS':
                        if self.dominates(run.fitness, local_best_fitness):
                            self.program.logger.debug(self.program.diff_patch(patch))
                            local_best_fitness = run.fitness
                            accept = True
                            if self.dominates(run.fitness, self.report['best_fitness']):
                                self.report['best_fitness'] = run.fitness
                                self.report['best_patch'] = patch
                                best = True
                                self.global_best = particle
                    self.hook_evaluation(patch, run, accept, best)
                    self.stats['steps'] += 1

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()

    def initialise_population(self):
        ParamEdit = self.config['possible_edits'][0]
        target_file = self.find_target_file_param()

        # 1st particle gets default value.
        starting_values = copy.deepcopy(self.program.contents[target_file]['current'])
        self.transform_category_to_int(starting_values)
        self.population.append(Particle(self.params, self.speed_max, self.speed_min, starting_values))

        # 2nd - Nth particle are randomly generated.
        for _ in range(self.pop_size - 1):
            starting_values = copy.deepcopy(ParamEdit.randomly_initialise_population(self.program))
            self.transform_category_to_int(starting_values)
            self.population.append(Particle(self.params, self.speed_max, self.speed_min, starting_values))

    def transform_category_to_int(self, starting_values):
        for param_id, realm in self.category_params.items():
            starting_values[param_id] = realm.get_data_index(starting_values[param_id])

    def transform_int_to_category(self, param_id, int_values):
        return copy.deepcopy(self.category_params[param_id].get_data_value(int_values))
    
    def create_particle_patch(self, particle):
        target_file = self.find_target_file_param()
        ParamEdit = self.config['possible_edits'][0]
        patch = Patch()
        for param_id, value in self.program.contents[target_file]['current'].items():
            if param_id in self.category_params:
                category_value = self.transform_int_to_category(param_id, particle.position[param_id])
                if category_value != value:
                    patch.edits.append(ParamEdit.create_with_input_value(target_file, param_id, category_value))
            elif particle.position[param_id] != value:
                patch.edits.append(ParamEdit.create_with_input_value(target_file, param_id, particle.position[param_id]))
        return patch

    def find_target_file_param(self):
        # return string of target_file that end with *.params
        for file in self.program.contents.keys():
            if file.endswith('.params'):
                return file

class Particle():
    def __init__(self, params, speed_max, speed_min, starting_values):
        self.position = dict()

        self.best = dict()
        self.best_fitness = None
        
        self.speed = dict()
        self.speed_max = speed_max
        self.speed_min = speed_min

        for param in params.keys():
            self.position[param] = starting_values[param]
            self.best[param] = starting_values[param]
            self.speed[param] = random.uniform(self.speed_min, self.speed_max)

    def __str__(self):
        return ('position: {position}\n'
            'speed: {speed}\n'
            'best: {best}\n'
            'best_fitness: {best_fitness}\n'
        ).format(**self.__dict__)
    
    def update_speed(self, global_best):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        c1 = c2 = 1.49
        for param_id, value in self.speed.items():
            new_speed = value + (c1 * r1 * (self.best[param_id] - self.position[param_id])) + (c2 * r2 * (global_best.position[param_id] - self.position[param_id]))
            
            if new_speed > self.speed_max:
                self.speed[param_id] = self.speed_max
            elif new_speed < self.speed_min:
                self.speed[param_id] = self.speed_min
            else:
                self.speed[param_id] = new_speed

    def update_position(self, spaces):
        for param_id, value in self.position.items():
            new_position = value + self.speed[param_id]

            # perform round up if the parameter is an integer
            if isinstance(spaces[param_id], (CategoricalRealm, GeometricRealm, UniformIntRealm)):
                new_position = round(new_position)

            # check for upper and lower bound
            lower_bound = spaces[param_id].start
            upper_bound = spaces[param_id].stop
            if new_position < lower_bound:
                self.position[param_id] = lower_bound
            elif new_position > upper_bound:
                self.position[param_id] = upper_bound
            else:
                self.position[param_id] = new_position
    
    def update_best(self, fitness):
        self.best = self.position
        self.best_fitness = fitness
            