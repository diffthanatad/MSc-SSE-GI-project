#!/bin/bash

END=10
for i in $(seq 1 $END); 
do
    CMD="./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_${i}.txt"
    $CMD; 
done
