python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_1.txt --patch _magpie_logs/minisat-hack_1690989310.patch
python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_10.txt --patch _magpie_logs/minisat-hack_1690991652.patch
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_1.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_2.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_3.txt
