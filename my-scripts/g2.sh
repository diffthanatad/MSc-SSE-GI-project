python3 -m bin.revalidate_patch --scenario scenario/AC/test_2.txt --patch _magpie_logs/minisat-hack_1690989316.patch
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_4.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_5.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_6.txt
python3 -m bin.local_search --scenario scenario/minisat/AC_GI/train_7.txt
