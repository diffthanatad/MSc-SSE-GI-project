#$ -S /bin/bash
#$ -l tmem=9G
#$ -l h_vmem=9G
#$ -N sat4j_train_1

export JAVA_HOME=/share/apps/openjdk-12.0.2
export PATH=/share/apps/openjdk-12.0.2/bin:$PATH
export LD_LIBRARY_PATH=/share/apps/openjdk-12.0.2/lib:$LD_LIBRARY_PATH

cd code/sat4j
time ./compile.sh
time ./run-sh/train_1.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
