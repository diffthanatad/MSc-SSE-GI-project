import copy
import random
import time

from ..base import Algorithm, Patch

class ParticleSwarmOptimization(Algorithm):
    param_list = list()
    param_size = 0
    pop_size = 10
    phi_1 = 2.0
    phi_2 = 2.0
    speed_max = 3
    speed_min = -3
    population = []

    global_best_particle = None # class Particle
    global_best_patch = None # class Patch
    # global_best = dict()
    # global_best_fitness = None
    global_best_run = None # class RunResult

    def setup(self):
        super().setup()
        self.name = 'Evolutionary Algorithm'        

    def run(self):
        try:
            # warmup
            self.hook_warmup()
            self.warmup()

            # start!
            self.hook_start()

            current_patch = self.report['best_patch']
            current_fitness = self.report['best_fitness']
            print(current_patch, current_fitness)

            # PSO set up.
            # how many parameters are there?
            for k, v in self.program.locations.items():
                if k.endswith('.params'):
                    self.param_list += v['param']
            self.param_size =  len(self.param_list)

            # initialise population and velocity at the same time
            self.initialise_population()

            # (1) evaluate fitness for each particle, for the first time.
            # (2) find initial global_best and global_fitness.
            # (3) report first best as 1st iteration.
            for i, particle in enumerate(self.population):
                patch = self.create_particle_patch(particle)
                run = self.evaluate_patch(patch)
                particle.fitness = run.fitness
                particle.best_fitness = run.fitness
                if run.status == 'SUCCESS':
                    print("****** yes =", run.fitness, "\n")
                else:
                    print("****** no =", run.fitness, "\n")
                
                if (i == 0):
                    self.global_best_particle = copy.deepcopy(self.population[0])
                    self.global_best_patch = copy.deepcopy(patch)
                    # self.global_best = copy.deepcopy(self.population[0].best)
                    # self.global_best_fitness = copy.deepcopy(self.population[0].best_fitness)
                    continue
                
                if isinstance(particle.best_fitness, float) and particle.best_fitness < self.global_best_fitness:
                    self.global_best_particle = copy.deepcopy(particle)
                    self.global_best_patch = copy.deepcopy(patch)
                    # self.global_best = copy.deepcopy(particle.best)
                    # self.global_best_fitness = copy.deepcopy(particle.best_fitness)
            # self.hook_evaluation(self.global_best_patch, self.global_best_run, )

            print("self.global_best:", self.global_best)
            print("self.global_best_fitness:", self.global_best_fitness)

            # main loop
            # current_patch = empty_patch from magpie/base/algorith.py/warmup();
            # reported global best which is the best configuration from the best particle.
            current_patch = self.report['best_patch']
            # current_fitness = time in second. How much time does it take to run the program during warmup.
            # reported global best which is the runtime of the best configuration from the best particle.
            current_fitness = self.report['best_fitness']
            
            # for each generation.
            # while not self.stopping_condition():
            #     self.hook_main_loop()
            #     current_patch, current_fitness = self.explore(current_patch, current_fitness)

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()
    
    def explore(self, current_patch, current_fitness):
        # for each particle.
        # (1) evaluate fitness value -> Find out and create a patch. -> send to self.evaluate_patch(patch)
        # for particle in self.population:
        #     patch = self.create_particle_patch(particle)
        #     # print(patch)
        #     # self.evaluate_patch(patch)
        #     run = self.evaluate_patch(patch)
        #     if run.status == 'SUCCESS':
        #         print("****** yes")
        #     else:
        #         print("****** no")

            # print(run)

        # move
        # for particle in self.population:
        #     pass

        # compare

        # accept -> Update the global best (i.e., best particle).
        
        # hook -> printing to the console.
        self.hook_evaluation(patch, run, accept, best)
        
        # next iteration
        self.stats['steps'] += 1
        return current_patch, current_fitness

    def initialise_population(self):
        ParamEdit = self.config['possible_edits'][0]

        # 1st particle is the default value.
        target_file = self.find_target_file_param()
        self.population.append(Particle(self.param_list, self.speed_max, self.speed_min, self.program.contents[target_file]['current']))

        # 2nd - Nth particle are randomly generated.
        for _ in range(self.pop_size - 1):
            starting_value = ParamEdit.randomly_initialise_population(self.program)
            self.population.append(Particle(self.param_list, self.speed_max, self.speed_min, starting_value))

    def create_particle_patch(self, particle):
        target_file = self.find_target_file_param()
        ParamEdit = self.config['possible_edits'][0]
        patch = Patch()
        for param_id, value in self.program.contents[target_file]['current'].items():
            if particle.position[param_id] != value:
                patch.edits.append(ParamEdit.create_with_input_value(target_file, param_id, particle.position[param_id]))
        return patch

    def find_target_file_param(self):
        # return string of target_file that end with *.params
        for file in self.program.contents.keys():
            if file.endswith('.params'):
                return file

class Particle():
    def __init__(self, param_list, speed_max, speed_min, starting_value):
        self.position = dict()
        self.fitness = None
        
        self.best = dict()
        self.best_fitness = None
        
        self.speed = dict()
        self.speed_max = speed_max
        self.speed_min = speed_min

        for param in param_list:
            self.position[param] = starting_value[param]
            self.best[param] = starting_value[param]
            self.speed[param] = random.uniform(self.speed_min, self.speed_max)

    def __str__(self):
        return ('position: {position}\n'
            'speed: {speed}\n'
            'best: {best}\n'
            'speed_max: {speed_max}\n'
            'speed_min: {speed_min}\n'
        ).format(**self.__dict__)