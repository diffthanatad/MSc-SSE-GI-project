#$ -S /bin/bash
#$ -l tmem=9G
#$ -l h_vmem=9G
#$ -N sat4j_train_gi_all
#$ -j y

source /share/apps/source_files/python/python-3.10.0.source
export JAVA_HOME=/share/apps/openjdk-12.0.2
export PATH=/share/apps/openjdk-12.0.2/bin:$PATH
export LD_LIBRARY_PATH=/share/apps/openjdk-12.0.2/lib:$LD_LIBRARY_PATH

cd MSc-SSE-GI-project
python3 -m bin.local_search --scenario scenario/sat4j/GI/train_1.txt
