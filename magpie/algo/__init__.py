from .local_search import LocalSearch, DummySearch, RandomSearch, RandomWalk, DebugSearch
from .local_search import FirstImprovement, BestImprovement, WorstImprovement, TabuSearch
from .genetic_programming import GeneticProgramming, GeneticProgrammingConcat, GeneticProgramming1Point, GeneticProgramming2Point, GeneticProgrammingUniformConcat, GeneticProgrammingUniformInter
from .validation import ValidSearch, ValidSingle, ValidTest, ValidRanking, ValidSimplify, ValidRankingSimplify
from .ablation import AblationAnalysis
from .evolutionary import ParticleSwarmOptimization

# "final" algos only
algos = [
    DummySearch, RandomSearch, RandomWalk, DebugSearch,
    FirstImprovement, BestImprovement, WorstImprovement, TabuSearch,
    GeneticProgrammingConcat, GeneticProgramming1Point, GeneticProgramming2Point, GeneticProgrammingUniformConcat, GeneticProgrammingUniformInter,
    ValidSingle, ValidTest, ValidRanking, ValidSimplify, ValidRankingSimplify,
    AblationAnalysis,
    ParticleSwarmOptimization
]
