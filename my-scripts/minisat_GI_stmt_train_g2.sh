#!/bin/sh

nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_2.txt > console-output/nohup_train_2.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_4.txt > console-output/nohup_train_4.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_6.txt > console-output/nohup_train_6.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_7.txt > console-output/nohup_train_7.txt &
nohup /usr/local/bin/python3.10 -m bin.local_search --scenario scenario/minisat_GI_stmt_train_8.txt > console-output/nohup_train_8.txt &
