python3 -m bin.revalidate_patch --scenario scenario/AC/test_3.txt --patch _magpie_logs/minisat-hack_1690989325.patch
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_8.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_9.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_10.txt
python3 -m bin.local_search --scenario scenario/minisat/GI/train_1.txt
