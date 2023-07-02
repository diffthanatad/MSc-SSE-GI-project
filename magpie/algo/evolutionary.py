import copy
import random
import time

from ..base import Algorithm, Patch

class ParticleSwarmOptimization(Algorithm):
    def setup(self):
        super().setup()
        self.name = 'Evolutionary Algorithm'
        self.config['pop_size'] = 10
        self.config['phi_1'] = 2.0
        self.config['phi_2'] = 2.0

        self.population = []
        self.velocities = []

    def run(self):
        try:
            # warmup
            self.hook_warmup()
            self.warmup()

            # start!
            self.hook_start()

            # initialise population and velocity
            self.initialise_population()
            self.initialise_velocities()
            print("population:", self.population)

            # main loop
            current_patch = self.report['best_patch']
            current_fitness = self.report['best_fitness']
            while not self.stopping_condition():
                self.hook_main_loop()
                current_patch, current_fitness = self.explore(current_patch, current_fitness)

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()
    
    def explore(self, current_patch, current_fitness):
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
        print("initialise_population()")
        ParamEdit = self.config['possible_edits'][0]
        for _ in range(self.config['pop_size']):
            self.population.append(ParamEdit.randomly_initialise_population(self.program))

    def initialise_velocities(self):
        print("initialise_velocities()")
        pass


        