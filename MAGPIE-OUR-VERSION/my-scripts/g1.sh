#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_1.txt --patch _magpie_logs/minisat-hack_1692606991.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_4.txt --patch _magpie_logs/minisat-hack_1692613302.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_5.txt --patch _magpie_logs/minisat-hack_1692615169.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_6.txt --patch _magpie_logs/minisat-hack_1692617047.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_7.txt --patch _magpie_logs/minisat-hack_1692618941.patch
