#!/bin/sh

nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_1.txt > console-output/nohup_train_1.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_2.txt > console-output/nohup_train_2.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_3.txt > console-output/nohup_train_3.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_4.txt > console-output/nohup_train_4.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_5.txt > console-output/nohup_train_5.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_6.txt > console-output/nohup_train_6.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_7.txt > console-output/nohup_train_7.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_8.txt > console-output/nohup_train_8.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_9.txt > console-output/nohup_train_9.txt &
nohup ./magpie.py local_search --scenario scenario/minisat_GI_stmt_train_10.txt > console-output/nohup_train_10.txt &