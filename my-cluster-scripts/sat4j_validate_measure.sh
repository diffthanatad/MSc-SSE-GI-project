#$ -S /bin/bash
#$ -l tmem=9G
#$ -l h_vmem=9G
#$ -N sat4j_train_1

export JAVA_HOME=/share/apps/openjdk-12.0.2
export PATH=/share/apps/openjdk-12.0.2/bin:$PATH
export LD_LIBRARY_PATH=/share/apps/openjdk-12.0.2/lib:$LD_LIBRARY_PATH

echo "Sat4j Validate Measure k-1 to k-10"

cd code/sat4j
time ./compile.sh
time ./run-sh/validate_1.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_2.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_3.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_4.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_5.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_6.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_7.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_8.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_9.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95
time ./run-sh/validate_10.sh -s Default -S RESTARTS=Glucose21Restarts,PHASE=RSATPhaseSelectionStrategy,SIMP=EXPENSIVE_SIMPLIFICATION,CLEANING=LBD2,PARAMS=SearchParams/claDecay:0.999/varDecay:0.95

ant clean