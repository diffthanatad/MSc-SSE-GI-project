#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_1.txt --patch _magpie_logs/minisat-hack_1692429363.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_2.txt --patch _magpie_logs/minisat-hack_1692440755.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_3.txt --patch _magpie_logs/minisat-hack_1692452100.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_4.txt --patch _magpie_logs/minisat-hack_1692463509.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_5.txt --patch _magpie_logs/minisat-hack_1692474881.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_6.txt --patch _magpie_logs/minisat-hack_1692429364.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_7.txt --patch _magpie_logs/minisat-hack_1692440705.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_8.txt --patch _magpie_logs/minisat-hack_1692452058.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_9.txt --patch _magpie_logs/minisat-hack_1692463407.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/validate_10.txt --patch _magpie_logs/minisat-hack_1692474732.patch
