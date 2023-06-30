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
        
        