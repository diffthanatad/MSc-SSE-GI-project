import copy
import math
import random
import time

from ..base import Algorithm, Patch
from .. import  params as params

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
                offsprings_temp = list()

                # first, new offsprings from two parents
                for _ in range(self.config['pop_size']):
                    parent1 = self.tournament_selection(pop)                    # selection
                    parent2 = self.tournament_selection(pop)

                    if random.random() <= self.config['crossover_rate']:
                        sol1, sol2 = self.crossover(parent1, parent2)           # crossover
                        self.mutate(sol1)                                       # mutation     
                        self.mutate(sol2)

                        offsprings_temp.append(sol1)
                        offsprings_temp.append(sol2)

                # second, new offsprings from initialisation             
                while len(offsprings_temp) < self.config['pop_size']:
                    sol = self.create_solution()
                    if sol in pop:
                        continue
                    offsprings_temp.append(sol)
                
                # elitisim
                parents = self.select(pop)
                copy_parents = copy.deepcopy(parents)
                k = int(self.config['pop_size']*self.config['offspring_elitism'])
                for parent in copy_parents[:k]:
                    offsprings.append(parent)
                N = self.config['pop_size'] - len(offsprings)
                offsprings += random.sample(offsprings_temp, N)

                # evaluate offsprings
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

    def mutate(self, chromosome: Patch) -> None:
        """ 
            chromosome = class Patch().edits
            gene = ParamSetting(('minisat_simplified.params', 'luby'), 'False')
            Update gene by reference. So, no return.
        """
        genes = chromosome.edits
        N = len(genes)
        to_delete = list()
        for i in range(N):
            if random.random() <= self.config['mutation_rate']:
                if isinstance(genes[i], params.ParamSetting):
                    # mutate parameter value
                    genes[i] = self.create_specific_edit(genes[i])
                elif random.random() <= self.config['delete_prob']:
                    # remove GI edit
                    to_delete.append(genes[i])

        for gene in to_delete:
            genes.remove(gene)
                                    
        if random.random() <= self.config['offspring_mutation']:
            # add new GI edit
            new_edit = self.create_edit_except_AC()
            genes.append(new_edit)

    def crossover(self, sol1: Patch, sol2: Patch) -> Patch:
        """"
            return a new solution of class Patch()
        """
        edits1 = copy.deepcopy(sol1.edits)
        edits2 = copy.deepcopy(sol2.edits)

        minimum = min(len(edits1), len(edits2))
        K = random.randint(1, minimum - 1)

        offspring1 = Patch(edits1[:K] + edits2[K:])
        offspring2 = Patch(edits2[:K] + edits1[K:])

        return offspring1, offspring2
        
    def filter(self, pop: dict) -> set[Patch]:
        tmp = {sol for sol in pop if pop[sol].status == 'SUCCESS'}
        return tmp

    def select(self, pop: dict) -> list[Patch]:
        """ 
            returns possible parents, ordered by fitness 
        """
        tmp = self.filter(pop)
        tmp = sorted(tmp, key=lambda sol: pop[sol].fitness)
        return tmp
    
    def create_solution(self) -> Patch:
        """
            create class Patch() which contains a list of class Edit() with random value for all parameters.
        """
        sol = self.create_all_edits()
        return Patch(sol)

    def tournament_selection(self, pop: dict) -> Patch:
        """
            return class Patch() of the best solution in the previous population from the tournament.
        """
        best = None
        best_fitness = None

        for _ in range(self.config['tournament_size']):
            sol = random.sample(list(pop), 1)[0]
            if best is None or self.dominates(pop[sol].fitness, best_fitness):
                best = sol
                best_fitness = pop[sol].fitness
        return best
