import copy
import math
import random
import time

from ..base import Algorithm, Patch
from ..params.params_edits import ParamSetting

class GeneticAlgorithm(Algorithm):
    category_params = list()
    int_params = list()

    def setup(self):
        super().setup()
        self.name = 'Genetic Algorithm'
        self.config['pop_size'] = 10
        self.config['delete_prob'] = 0.5

        self.config['cxpb_chrm'] = 0.9
        self.config['cxpb_gene'] = 0.9
        self.config['mutpb_chrm'] = 0.2
        self.config['mutpb_gene'] = 0.1
        
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

            self.category_params = self.get_categorical_parameters()
            self.int_params = self.get_int_parameters()

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

                offsprings = self.tournament_selection(self.config['pop_size'], self.config['tournament_size'], pop)
                offsprings = copy.deepcopy(offsprings)
                
                for i in range(1, self.config['pop_size'], 2):
                    if random.random() <= self.config['cxpb_chrm']:
                        # print("before:", offsprings[i-1])
                        # print(offsprings[i])
                        self.crossover(offsprings[i-1], offsprings[i])
                        # print("after:", offsprings[i-1])
                        # print(offsprings[i])
                        # print()
                for i in range(self.config['pop_size']):
                    if random.random() <= self.config['mutpb_chrm']:
                        self.mutate(offsprings[i])
                break

                # first, new offsprings from two parents
                # for _ in range(self.config['pop_size']):
                #     parent1 = self.tournament_selection(pop)                    # selection
                #     parent2 = self.tournament_selection(pop)

                #     if random.random() <= self.config['crossover_rate']:
                #         sol1, sol2 = self.crossover(parent1, parent2)           # crossover
                #         self.mutate(sol1)                                       # mutation     
                #         self.mutate(sol2)

                #         offsprings_temp.append(sol1)
                #         offsprings_temp.append(sol2)

                # # second, new offsprings from initialisation             
                # while len(offsprings_temp) < self.config['pop_size']:
                #     sol = self.create_solution()
                #     if sol in pop:
                #         continue
                #     offsprings_temp.append(sol)
                
                # # elitisim
                # parents = self.select(pop)
                # copy_parents = copy.deepcopy(parents)
                # k = int(self.config['pop_size']*self.config['offspring_elitism'])
                # for parent in copy_parents[:k]:
                #     offsprings.append(parent)
                # N = self.config['pop_size'] - len(offsprings)
                # offsprings += random.sample(offsprings_temp, N)

                # # evaluate offsprings
                # pop.clear()
                # local_best = None
                # local_best_fitness = None
                # for sol in offsprings:
                #     if self.stopping_condition():
                #         break
                #     run = self.evaluate_patch(sol)
                #     accept = best = False
                #     if run.status == 'SUCCESS':
                #         if self.dominates(run.fitness, local_best_fitness):
                #             self.program.logger.debug(self.program.diff_patch(sol))
                #             local_best_fitness = run.fitness
                #             local_best = sol
                #             accept = True
                #             if self.dominates(run.fitness, self.report['best_fitness']):
                #                 self.report['best_fitness'] = run.fitness
                #                 self.report['best_patch'] = sol
                #                 best = True
                #     self.hook_evaluation(sol, run, accept, best)
                #     pop[sol] = run
                #     self.stats['steps'] += 1

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
        edits = chromosome.edits
        N = len(edits)
        for i in range(N):
            if random.random() <= self.config['mutpb_gene']:
                if isinstance(edits[i], ParamSetting):
                    edits[i] = self.create_specific_edit(edits[i])
                else:
                    # GI
                    print("************ GI is here!!!, mutate();")
                    continue

    def crossover(self, ind1: Patch, ind2: Patch) -> Patch:
        """ Crossover is performed via reference. """
        edit1 = ind1.edits
        edit2 = ind2.edits
        N = len(edit1)
        for i in range(N):
            if random.random() > self.config['cxpb_gene']:
                continue
            if isinstance(edit1[i], ParamSetting) and isinstance(edit2[i], ParamSetting):
                param_id_1 = edit1[i].target[1]
                value_1 = edit1[i].data[0]
                value_2 = edit2[i].data[0]

                target_file = self.get_target_file_for_parameter(param_id_1)

                if param_id_1 in self.category_params:
                    edit1[i], edit2[i] = edit2[i], edit1[i]
                elif value_1 <= value_2:
                    if param_id_1 in self.int_params:
                        edit1[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_1, value_2))
                        edit2[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_1, value_2))
                    else:
                        edit1[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_1, value_2))
                        edit2[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_1, value_2))
                elif value_1 > value_2:
                    if param_id_1 in self.int_params:
                        edit1[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_2, value_1))
                        edit2[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_2, value_1))
                    else:
                        edit1[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_2, value_1))
                        edit2[i] = ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_2, value_1))
            else:
                # GI
                print("************ GI is here!!!, crossover();")
                continue
        
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

    def tournament_selection(self, k: int, tournament_size: int, pop: dict) -> list[Patch]:
        """
            :param k: Number of inidividual to select
            :param tournament_size: Number of individual participating in each tournament.
            :return: A list of class Patch() of the best solution in the previous population from the tournament.
        """
        chosen = list()
        for _ in range(k):
            solutions = random.sample(list(pop), tournament_size)
            best = None
            best_fitness = None
            for sol in solutions:
                if best is None or self.dominates(pop[sol].fitness, best_fitness):
                    best = sol
                    best_fitness = pop[sol].fitness
            chosen.append(best)
        return chosen
