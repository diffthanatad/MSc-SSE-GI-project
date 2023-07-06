import copy
import random
import time

from ..base import Algorithm, Patch
from ..params import CategoricalRealm, GeometricRealm, UniformIntRealm

class ParticleSwarmOptimization(Algorithm):
    params = dict()                     # magpie.params.realms
    param_size = 0
    pop_size = 5
    speed_max = 3
    speed_min = -3
    population = list()                 # class Particle

    global_best_particle = None         # class Particle
    global_best_patch = None            # class Patch

    generation_best_particle = None     # class Particle
    generation_best_patch = None        # class Patch

    category_params = dict()            # class CategoricalRealm

    def setup(self):
        super().setup()
        self.name = 'Evolutionary Algorithm'        

    def run(self):
        try:
            # warmup
            self.hook_warmup()
            self.warmup()

            # PSO set up.
            # (1) how many parameters are there?
            target_file = self.find_target_file_param()
            self.params.update(self.program.contents[target_file]['space'])
            self.param_size = len(self.params)
            # (2) search for categorical params
            for param_id, value in self.program.contents[target_file]['space'].items():
                if isinstance(value, CategoricalRealm):
                    self.category_params[param_id] = value

            self.initialise_population() # initialise population and velocity at the same time

            # start!
            self.hook_start() 
            self.evaluate_generation_1() # evaluate 1st generation
            self.report_best()

            # evaluate 2nd - nth generation
            current_patch = self.report['best_patch']
            current_fitness = self.report['best_fitness']
            while not self.stopping_condition():
                # reset generation_best
                self.generation_best_particle = None
                self.generation_best_patch = None

                # start exploring each generation
                self.hook_main_loop()
                current_patch, current_fitness = self.explore(current_patch, current_fitness)

                self.report_best()

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()
    
    def explore(self, current_patch, current_fitness):
        for particle in self.population:
            # update speed and position
            particle.update_speed(self.global_best_particle)
            particle.update_position(self.params)

            # evaluate
            patch = self.create_particle_patch(particle)
            particle.position_run = self.evaluate_patch(patch)
            print("explore:", particle.position_run.fitness)

            # update particle best
            if self.dominates(particle.position_run.fitness, particle.best_run.fitness):
                particle.best = particle.position
                particle.best_run = particle.position_run
        
        self.generation_best_particle = self.population[0]
        self.generation_best_patch    = self.create_particle_patch(self.population[0])
        
        accept = best = False
        
        # find generation_best_particle
        for particle in self.population:
            if self.dominates(particle.position_run.fitness, self.generation_best_particle.position_run.fitness):
                accept = True
                
                self.generation_best_particle = particle
                self.generation_best_patch = self.create_particle_patch(particle)
        
        # update global_best_particle
        if self.dominates(self.generation_best_particle.best_run.fitness, self.report['best_fitness']):
            best = True
            
            self.report['best_fitness'] = self.generation_best_particle.best_run.fitness
            self.report['best_patch']   = self.generation_best_patch

            self.global_best_particle = self.generation_best_particle
            self.global_best_patch    = self.generation_best_patch
        
        self.hook_evaluation(self.generation_best_patch, self.generation_best_particle.position_run, accept, best)
        self.stats['steps'] += 1
        
        return self.generation_best_patch, self.generation_best_particle.best_run.fitness

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
    
    def evaluate_generation_1(self):
        for particle in self.population:
           patch = self.create_particle_patch(particle)
           particle.position_run = particle.best_run = self.evaluate_patch(patch)
        
        self.generation_best_particle = self.global_best_particle = self.population[0]
        self.generation_best_patch    = self.global_best_patch    = Patch()
        
        accept = best = False

        # find generation_best_particle
        for particle in self.population:
            if self.dominates(particle.best_run.fitness, self.generation_best_particle.best_run.fitness):
                accept = True
                
                self.generation_best_particle = particle
                self.generation_best_patch = self.create_particle_patch(particle)
        
        # find global_best_particle
        if self.dominates(self.generation_best_particle.best_run.fitness, self.report['best_fitness']):
            best = True
            
            self.report['best_fitness'] = self.generation_best_particle.best_run.fitness
            self.report['best_patch']   = self.generation_best_patch

            self.global_best_particle = self.generation_best_particle
            self.global_best_patch    = self.generation_best_patch

        self.report_best()

        self.hook_evaluation(self.generation_best_patch, self.generation_best_particle.best_run, accept, best)
        self.stats['steps'] += 1
    
    def report_best(self):
        print("report: global", self.global_best_particle.best_run.fitness, "generation", self.generation_best_particle.position_run.fitness)
    
class Particle():
    def __init__(self, params, speed_max, speed_min, starting_values):
        self.position = dict()
        self.position_run = None        # class RunResult

        self.best = dict()
        self.best_run = None            # class RunResult
        
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
        ).format(**self.__dict__)
    
    def update_speed(self, global_best):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        c1 = c2 = 1.49
        for param_id, value in self.speed.items():
            self.speed[param_id] = value + (c1 * r1 * (self.best[param_id] - self.position[param_id])) + (c2 * r2 * (global_best.position[param_id] - self.position[param_id]))

    def update_position(self, spaces):
        for param_id, value in self.position.items():
            new_position = value + self.speed[param_id]

            # perform round up if the parameter is an integer
            if isinstance(spaces[param_id], (CategoricalRealm, GeometricRealm, UniformIntRealm)):
                print("rounding up", param_id, new_position, end=", ")
                new_position = round(new_position)
                print(new_position, end=", ")

            # check for upper and lower bound
            lower_bound = spaces[param_id].start
            upper_bound = spaces[param_id].stop
            if new_position < lower_bound:
                self.position[param_id] = lower_bound
            elif new_position > upper_bound:
                self.position[param_id] = upper_bound
            else:
                self.position[param_id] = new_position
            
            print(self.position[param_id])
            
