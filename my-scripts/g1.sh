#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_1.txt --patch _magpie_logs/minisat-hack_1692371461.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_2.txt --patch _magpie_logs/minisat-hack_1692382819.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_3.txt --patch _magpie_logs/minisat-hack_1692394207.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_4.txt --patch _magpie_logs/minisat-hack_1692405859.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_5.txt --patch _magpie_logs/minisat-hack_1692417279.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_6.txt --patch _magpie_logs/minisat-hack_1692371462.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_7.txt --patch _magpie_logs/minisat-hack_1692382794.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_8.txt --patch _magpie_logs/minisat-hack_1692394183.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_9.txt --patch _magpie_logs/minisat-hack_1692405812.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/validate_10.txt --patch _magpie_logs/minisat-hack_1692417149.patch
