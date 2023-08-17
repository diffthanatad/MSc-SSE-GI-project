#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_1.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_2.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_3.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_4.txt
python3 -m bin.genetic_algorithm --scenario scenario/minisat/GI/train_5.txt

