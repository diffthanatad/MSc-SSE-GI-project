#!/bin/bash

source /share/apps/source_files/python/python-3.10.0.source
export JAVA_HOME=/share/apps/openjdk-12.0.2
export PATH=/share/apps/openjdk-12.0.2/bin:$PATH
export LD_LIBRARY_PATH=/share/apps/openjdk-12.0.2/lib:$LD_LIBRARY_PATH

python3 -m bin.local_search --scenario scenario/sat4j/GI/train_${SGE_TASK_ID}.txt
