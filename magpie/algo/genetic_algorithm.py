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
        self.config['tournament_size'] = 3

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
                sol = self.create_solution()
                if sol in pop:
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
            while not self.stopping_condition():
                self.stats['gen'] += 1
                self.hook_main_loop()
                offsprings = list()
                
                # selection, parents = [<magpie.base.patch.Patch object at 0x7f939cb3ac50>, ...]
                parents = self.select(pop)
                
                # elitism
                copy_parents = copy.deepcopy(parents)
                ELITISM_NUM = int(self.config['pop_size']*self.config['offspring_elitism'])
                for parent in copy_parents[:ELITISM_NUM]:
                    offsprings.append(parent)

                # crossover
                copy_parents = copy.deepcopy(parents)
                for parent1 in copy_parents:
                    parent2 = copy.deepcopy(random.sample(parents, 1)[0])
                    if random.random() <= self.config['crossover_rate']:
                        sol = self.crossover(parent1, parent2)
                        offsprings.append(sol)

                # mutation
                for offspring in offsprings[ELITISM_NUM:]:
                    self.mutate(offspring)
                
                # regrow                
                while len(offsprings) < self.config['pop_size']:
                    sol = self.create_solution()
                    if sol in pop:
                        continue
                    offsprings.append(sol)
                
                if len(offsprings) != self.config['pop_size']:
                    print("****", len(offspring))
                
                # replace
                pop.clear()
                local_best = None
                local_best_fitness = None
                for sol in offsprings:
                    if self.stopping_condition():
                        break
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

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()

    def mutate(self, chromosome):
        """ 
            chromosome = class Patch().edits
            gene = ParamSetting(('minisat_simplified.params', 'luby'), 'False')
            Update gene by reference. So, no return.
        """
        genes = chromosome.edits
        N = len(genes)
        for i in range(N):
            if random.random() <= self.config['mutation_rate']:
                genes[i] = self.create_specific_edit(genes[i])

    def crossover(self, sol1, sol2):
        """"
            return a new solution of class Patch()
        """
        edits1 = copy.deepcopy(sol1.edits)
        edits2 = copy.deepcopy(sol2.edits)
        N = len(edits1)
        K = random.randrange(1, N - 1)

        offspring1 = Patch(edits1[:K] + edits2[K:])
        offspring2 = Patch(edits2[:K] + edits1[K:])

        return offspring1
        
    def filter(self, pop):
        tmp = {sol for sol in pop if pop[sol].status == 'SUCCESS'}
        return tmp

    def select(self, pop):
        """ 
            returns possible parents, ordered by fitness 
        """
        tmp = self.filter(pop)
        tmp = sorted(tmp, key=lambda sol: pop[sol].fitness)
        return tmp
    
    def create_solution(self):
        """
            create class Patch() which contains a list of class Edit() with random value for all parameters.
        """
        sol = self.create_all_edits()
        return Patch(sol)
