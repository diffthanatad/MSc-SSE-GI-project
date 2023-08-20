#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_1.txt --patch _magpie_logs/minisat-hack_1692371463.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_2.txt --patch _magpie_logs/minisat-hack_1692382852.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_3.txt --patch _magpie_logs/minisat-hack_1692394265.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_4.txt --patch _magpie_logs/minisat-hack_1692405876.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_5.txt --patch _magpie_logs/minisat-hack_1692417306.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_6.txt --patch _magpie_logs/minisat-hack_1692429365.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_7.txt --patch _magpie_logs/minisat-hack_1692440722.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_8.txt --patch _magpie_logs/minisat-hack_1692452066.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_9.txt --patch _magpie_logs/minisat-hack_1692463410.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/validate_10.txt --patch _magpie_logs/minisat-hack_1692474735.patch
