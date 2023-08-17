#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_6.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_7.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_8.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_9.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_10.txt

