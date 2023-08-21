#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/test_6.txt --patch _magpie_logs/minisat-hack_1692617226.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/test_9.txt --patch _magpie_logs/minisat-hack_1692623780.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/test_10.txt --patch _magpie_logs/minisat-hack_1692625555.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/test_3.txt --patch _magpie_logs/minisat-hack_1692611498.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/test_4.txt --patch _magpie_logs/minisat-hack_1692613457.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/GI/test_6.txt --patch _magpie_logs/minisat-hack_1692617955.patch
