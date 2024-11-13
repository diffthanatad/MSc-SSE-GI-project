#$ -S /bin/bash
#$ -l tmem=7.5G
#$ -l h_vmem=7.5G
#$ -N te_gi_all
#$ -t 1-8
#$ -wd /home/tsongpet/MSc-SSE-GI-project
#$ -j y
#$ -l hostname=burns-610-43|fry-611-118

source /share/apps/source_files/python/python-3.10.0.source
export JAVA_HOME=/share/apps/openjdk-12.0.2
export PATH=/share/apps/openjdk-12.0.2/bin:$PATH
export LD_LIBRARY_PATH=/share/apps/openjdk-12.0.2/lib:$LD_LIBRARY_PATH

COMMAND=$(sed -n ${SGE_TASK_ID}'{p;q}' my-cluster-scripts/test.txt)

echo $COMMAND

$COMMAND
