#!/bin/csh
source /opt/Python/Python-3.10.1_Setup.csh

python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_8.txt --patch _magpie_logs/minisat-hack_1692620962.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_9.txt --patch _magpie_logs/minisat-hack_1692622713.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_10.txt --patch _magpie_logs/minisat-hack_1692624637.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/test_3.txt --patch _magpie_logs/minisat-hack_1692611221.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC_GI/test_4.txt --patch _magpie_logs/minisat-hack_1692613161.patch
