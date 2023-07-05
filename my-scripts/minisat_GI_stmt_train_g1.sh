#!/bin/sh

./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_1.txt
./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_3.txt
./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_5.txt
./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_9.txt
./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_10.txt 

nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_1.txt > console-output/nohup_train_1.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_3.txt > console-output/nohup_train_3.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_5.txt > console-output/nohup_train_5.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_9.txt > console-output/nohup_train_9.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_10.txt > console-output/nohup_train_10.txt &

