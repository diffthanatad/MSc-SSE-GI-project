import copy
import math
import random
import time

from ..base import Algorithm, Patch

class GeneticAlgorithm(Algorithm):
    def setup(self):
        super().setup()
        self.name = 'Genetic Algorithm'
        self.config['pop_size'] = 10
        self.config['delete_prob'] = 0.5
        self.config['offspring_elitism'] = 0.1
        self.config['offspring_crossover'] = 0.5
        self.config['offspring_mutation'] = 0.4
        
        self.config['crossover_rate'] = 0.5
        self.config['mutation_rate'] = 0.1

    def reset(self):
        super().reset()
        self.stats['gen'] = 0

    def aux_log_counter(self):
        return '{}-{}'.format(self.stats['gen'], self.stats['steps']%self.config['pop_size']+1)

    def run(self):
        try:
            # warmup
            self.hook_warmup()
            self.warmup()

            # start!
            self.hook_start()

            # initial pop
            pop = dict()
            local_best = None
            local_best_fitness = None
            while len(pop) < self.config['pop_size']:
                sol = self.initialise_solution()
                if sol in pop:
                    print("**** duplicate solution")
                    continue
                run = self.evaluate_patch(sol)
                accept = best = False
                if run.status == 'SUCCESS':
                    if self.dominates(run.fitness, local_best_fitness):
                        self.program.logger.debug(self.program.diff_patch(sol))
                        local_best_fitness = run.fitness
                        local_best = sol
                        accept = True
                        if self.dominates(run.fitness, self.report['best_fitness']):
                            self.report['best_fitness'] = run.fitness
                            self.report['best_patch'] = sol
                            best = True
                self.hook_evaluation(sol, run, accept, best)
                pop[sol] = run
                self.stats['steps'] += 1

            # main loop
            # while not self.stopping_condition():
            for i in range(1):
                self.stats['gen'] += 1
                self.hook_main_loop()
                offsprings = list()
                parents = self.select(pop)
                # elitism
                copy_parents = copy.deepcopy(parents)
                k = int(self.config['pop_size']*self.config['offspring_elitism'])
                for parent in copy_parents[:k]:
                    offsprings.append(parent)
                # crossover
                copy_parents = copy.deepcopy(parents)
                for parent1 in copy_parents:
                    parent2 = copy.deepcopy(random.sample(parents, 1)[0])
                    if random.random() <= self.config['crossover_rate']:
                        sol = self.crossover(parent1, parent2)
                        offsprings.append(sol)

                    # if random.random() <= 0.5:
                    #     sol = self.crossover(parent, sol)
                    # else:
                    #     sol = self.crossover(sol, parent)
                    # offsprings.append(sol)
            #     # mutation
            #     copy_parents = copy.deepcopy(parents)
            #     k = int(self.config['pop_size']*self.config['offspring_mutation'])
            #     for parent in copy_parents[:k]:
            #         self.mutate(parent)
            #         offsprings.append(parent)
            #     # regrow
            #     while len(offsprings) < self.config['pop_size']:
            #         sol = Patch()
            #         self.mutate(sol)
            #         if sol in pop:
            #             continue
            #         offsprings.append(sol)
            #     # replace
            #     pop.clear()
            #     local_best = None
            #     local_best_fitness = None
            #     for sol in offsprings:
            #         if self.stopping_condition():
            #             break
            #         run = self.evaluate_patch(sol)
            #         accept = best = False
            #         if run.status == 'SUCCESS':
            #             if self.dominates(run.fitness, local_best_fitness):
            #                 self.program.logger.debug(self.program.diff_patch(sol))
            #                 local_best_fitness = run.fitness
            #                 local_best = sol
            #                 accept = True
            #                 if self.dominates(run.fitness, self.report['best_fitness']):
            #                     self.report['best_fitness'] = run.fitness
            #                     self.report['best_patch'] = sol
            #                     best = True
            #         self.hook_evaluation(sol, run, accept, best)
            #         pop[sol] = run
            #         self.stats['steps'] += 1

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()

    def mutate(self, patch):
        """ Needs to update to make it matches GA. """
        if patch.edits and random.random() < self.config['delete_prob']:
            del patch.edits[random.randrange(0, len(patch.edits))]
        else:
            patch.edits.append(self.create_edit())

    def crossover(self, sol1, sol2):
        
        parent1 = copy.deepcopy(sol1.edits)
        parent2 = copy.deepcopy(sol2.edits)
        N = len(parent1.edits)
        K = random.randrange(1, N - 1)

        print(type(parent1), type(parent2))
        print(parent1, parent2)

        offspring1 = Patch(parent1[:K] + parent2[K:])
        offspring2 = Patch(parent2[:K] + parent1[K:])

        print(offspring1, offspring2)
        return offspring1, offspring2
        
    def filter(self, pop):
        tmp = {sol for sol in pop if pop[sol].status == 'SUCCESS'}
        return tmp

    def select(self, pop):
        """ returns possible parents ordered by fitness """
        tmp = self.filter(pop)
        tmp = sorted(tmp, key=lambda sol: pop[sol].fitness)
        return tmp
    
    def initialise_solution(self):
        sol = self.create_all_edits()
        return Patch(sol)
