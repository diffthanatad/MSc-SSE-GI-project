import copy
import random
import time

from ..base import Algorithm, Patch

class ParticleSwarmOptimization(Algorithm):
    param_list = list()
    param_size = 0
    pop_size = 3
    phi_1 = 2.0
    phi_2 = 2.0
    speed_max = 3
    speed_min = -3
    population = []
    speeds = []

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

            # print("evolutionary.py - self.program:", self.program.contents)
            # print(self.program.local_contents)
            # print(self.program.locations)

            # how many parameters are there?
            for k, v in self.program.locations.items():
                if k.endswith('.params'):
                    self.param_list += v['param']
            self.param_size =  len(self.param_list)

            # initialise population and velocity at the same time
            self.initialise_population()

            # main loop
            current_patch = self.report['best_patch'] # empty patch from magpie/base/algorith.py/warmup();
            current_fitness = self.report['best_fitness'] # Time in seconds. How much time does it take to run the program during warmup.
            
            # for each generation.
            while not self.stopping_condition():
                self.hook_main_loop()
                current_patch, current_fitness = self.explore(current_patch, current_fitness)

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()
    
    def explore(self, current_patch, current_fitness):
        # for each particle.
        for part in self.population:
            print(str(part))
            # run = self.evaluate_patch(patch)
            # evaluate fitness
            pass

        # move
        for particle in self.population:
            pass

        # compare

        # accept -> Update the global best (i.e., best particle).
        
        # hook -> printing to the console.
        self.hook_evaluation(patch, run, accept, best)
        
        # next iteration
        self.stats['steps'] += 1
        return current_patch, current_fitness

    def initialise_population(self):
        ParamEdit = self.config['possible_edits'][0]
        for _ in range(self.pop_size):
            starting_value = ParamEdit.randomly_initialise_population(self.program)
            self.population.append(Particle(self.param_list, self.speed_max, self.speed_min, starting_value))

    # def initialise_population(self):
    #     ParamEdit = self.config['possible_edits'][0]
    #     for _ in range(self.config['pop_size']):
    #         self.population.append(ParamEdit.randomly_initialise_population(self.program))

    # def initialise_velocities(self):
    #     for _ in range(self.config['pop_size']):
    #         particle_speeds = []
    #         for _ in range(self.config['param_size']):
    #             particle_speeds.append(random.uniform(self.config['speed_min'], self.config['speed_max']))
    #         self.speeds.append(particle_speeds)
    #     pass

class Particle():
    def __init__(self, param_list, speed_max, speed_min, starting_value):
        self.position = dict()
        self.speed = dict()
        self.best = dict()
        self.speed_max = speed_max
        self.speed_min = speed_min

        for param in param_list:
            self.position[param] = starting_value[param]
            self.speed[param] = random.uniform(self.speed_min, self.speed_max)
            self.best[param] = starting_value[param]

    def __str__(self):
        return ('position: {position}\n'
            'speed: {speed}\n'
            'best: {best}\n'
            'speed_max: {speed_max}\n'
            'speed_min: {speed_min}\n'
        ).format(**self.__dict__)