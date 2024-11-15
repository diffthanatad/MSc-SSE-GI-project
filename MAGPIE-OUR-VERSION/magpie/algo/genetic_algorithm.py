import copy
import math
import random
import time
from itertools import zip_longest

from ..base import Algorithm, Patch
from ..params.params_edits import ParamSetting

class Chromosome:
    def __init__(self, genes, fitness, status):
        self.genes = genes
        self.fitness = fitness
        self.status = status
    
    def get_fitness(self):
        return self.fitness
    
    def get_genes(self):
        return self.genes

    def get_status(self):
        return self.status

class GeneticAlgorithm(Algorithm):
    category_params = list()
    int_params = list()
    exist_GI_possible_edits = False

    def setup(self):
        super().setup()
        self.name = 'Genetic Algorithm'
        self.config['pop_size'] = 10
        self.config['elitism_size'] = 2

        self.config['cxpb_chrm'] = 0.5
        self.config['cxpb_gene'] = 0.5
        self.config['mutpb_chrm'] = 0.2
        self.config['mutpb_gene'] = 0.1
        self.config['GI_delete_prob'] = 0.5
        self.config['GI_create_prob'] = 0.5
        
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
            self.exist_GI_possible_edits = self.get_exist_GI_possible_edits()

            # initial pop
            pop = list()
            local_best_fitness = None
            for i in range(self.config['pop_size']):
                sol = self.create_solution()
                if i >= self.config['elitism_size']:
                    self.pre_mutate(sol)
                sol_minimal = self.remove_edits_with_default_value_from_patch(sol)
                run = self.evaluate_patch(sol_minimal)
                accept = best = False
                if run.status == 'SUCCESS':
                    if self.dominates(run.fitness, local_best_fitness):
                        self.program.logger.debug(self.program.diff_patch(sol_minimal))
                        local_best_fitness = run.fitness
                        accept = True
                        if self.dominates(run.fitness, self.report['best_fitness']):
                            self.report['best_fitness'] = run.fitness
                            self.report['best_patch'] = sol_minimal
                            best = True
                self.hook_evaluation(sol_minimal, run, accept, best)
                pop.append(Chromosome(sol, run.fitness, run.status))
                self.stats['steps'] += 1

            # main loop
            while not self.stopping_condition():
                self.stats['gen'] += 1
                self.hook_main_loop()
                
                offsprings = list() # list[Patch]
                temp = self.select(pop)
                for individual in temp[:self.config['elitism_size']:]:
                    offsprings.append(copy.deepcopy(individual))
                
                temp = self.tournament_selection(self.config['pop_size'] - self.config['elitism_size'], self.config['tournament_size'], pop)
                for individual in temp:
                    offsprings.append(copy.deepcopy(individual))
                
                for i in range(1, self.config['pop_size'], 2):
                    if random.random() <= self.config['cxpb_chrm']:
                        offsprings[i-1], offsprings[i] = self.crossover(offsprings[i-1], offsprings[i])

                for i in range(self.config['pop_size']):
                    if random.random() <= self.config['mutpb_chrm']:
                        self.mutate(offsprings[i])

                # evaluate offsprings
                pop.clear()
                local_best_fitness = None
                for sol in offsprings:
                    if self.stopping_condition():
                        break
                    sol_minimal = self.remove_edits_with_default_value_from_patch(sol)
                    run = self.evaluate_patch(sol_minimal)
                    accept = best = False
                    if run.status == 'SUCCESS':
                        if self.dominates(run.fitness, local_best_fitness):
                            self.program.logger.debug(self.program.diff_patch(sol_minimal))
                            local_best_fitness = run.fitness
                            accept = True
                            if self.dominates(run.fitness, self.report['best_fitness']):
                                self.report['best_fitness'] = run.fitness
                                self.report['best_patch'] = sol_minimal
                                best = True
                    self.hook_evaluation(sol_minimal, run, accept, best)
                    pop.append(Chromosome(sol, run.fitness, run.status))
                    self.stats['steps'] += 1

        except KeyboardInterrupt:
            self.report['stop'] = 'keyboard interrupt'

        finally:
            # the end
            self.hook_end()

    def pre_mutate(self, chromosome: Patch) -> None:
        edits = chromosome.edits
        N = len(edits)
        for i in range(N):
            if random.random() <= self.config['mutpb_gene']:
                if isinstance(edits[i], ParamSetting):
                    edits[i] = self.create_specific_edit(edits[i])
        if self.exist_GI_possible_edits and random.random() <= self.config['GI_create_prob']:
            edits.append(self.create_GI_edit())

    def mutate(self, chromosome: Patch) -> None:
        """ 
            chromosome = class Patch().edits
            gene = ParamSetting(('minisat_simplified.params', 'luby'), 'False')
            Update gene by reference. So, no return.
        """
        GI_delete_index = list()
        edits = chromosome.edits
        N = len(edits)
        for i in range(N):
            if random.random() <= self.config['mutpb_gene']:
                if isinstance(edits[i], ParamSetting):
                    edits[i] = self.create_specific_edit(edits[i])
                else:
                    GI_delete_index.append(i)
        
        # delete GI edit(s) and shrink the Patch size.
        for i in GI_delete_index[::-1]:
            del edits[i]

        # add one new GI edit.
        if self.exist_GI_possible_edits and random.random() <= self.config['GI_create_prob']:
            edits.append(self.create_GI_edit())

    def crossover(self, ind1: Patch, ind2: Patch) -> Patch:
        new_edit1 = list()
        new_edit2 = list()
        original_edits = list(zip_longest(ind1.edits, ind2.edits))

        for edit1, edit2 in original_edits:
            if random.random() > self.config['cxpb_gene']:
                new_edit1.append(edit1)
                new_edit2.append(edit2)
                continue
            if isinstance(edit1, ParamSetting) and isinstance(edit2, ParamSetting):
                param_id_1 = edit1.target[1]
                value_1 = edit1.data[0]
                value_2 = edit2.data[0]
                target_file = self.get_target_file_for_parameter(param_id_1)

                if param_id_1 in self.category_params:
                    new_edit1.append(edit2)
                    new_edit2.append(edit1)
                elif value_1 <= value_2:
                    if param_id_1 in self.int_params:
                        new_edit1.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_1, value_2)) )
                        new_edit2.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_1, value_2)) )
                    else:
                        new_edit1.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_1, value_2)) )
                        new_edit2.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_1, value_2)) )
                elif value_1 > value_2:
                    if param_id_1 in self.int_params:
                        new_edit1.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_2, value_1)) )
                        new_edit2.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.randint(value_2, value_1)) )
                    else:
                        new_edit1.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_2, value_1)) )
                        new_edit2.append( ParamSetting.create_with_input_value(target_file, param_id_1, random.uniform(value_2, value_1)) )
            else:
                new_edit1.append(edit2)
                new_edit2.append(edit1)
        while(None in new_edit1):
            new_edit1.remove(None)
        while(None in new_edit2):
            new_edit2.remove(None)
        return Patch(copy.deepcopy(new_edit1)), Patch(copy.deepcopy(new_edit2))

    def create_solution(self) -> Patch:
        """
            create class Patch() which contains a list of class Edit() with random value for all parameters.
        """
        sol = self.create_all_default_edits_for_one_chrm()
        return Patch(sol)

    def tournament_selection(self, k: int, tournament_size: int, pop: list[Chromosome]) -> list[Patch]:
        """
            :param k: Number of inidividual to select
            :param tournament_size: Number of individual participating in each tournament.
            :return: A list of class Patch() of the best solution in the previous population from the tournament.
        """
        chosen = list()
        for _ in range(k):
            solutions = random.sample(pop, tournament_size)
            best = None
            best_fitness = None
            for sol in solutions:
                if best is None or self.dominates(sol.get_fitness(), best_fitness):
                    best = sol.get_genes()
                    best_fitness = sol.get_fitness()
            chosen.append(best)
        return chosen

    def filter(self, pop: list[Chromosome]) -> set[Chromosome]:
        tmp = {sol for sol in pop if sol.get_status() == 'SUCCESS'}
        return tmp

    def select(self, pop: list[Chromosome]) -> list[Patch]:
        """ returns possible parents ordered by fitness """
        tmp = self.filter(pop)
        tmp = sorted(tmp, key=lambda sol: sol.get_fitness())
        patches = list()
        for chromosome in tmp:
            patches.append(chromosome.get_genes())
        return patches