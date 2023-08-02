python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_7.txt --patch _magpie_logs/minisat-hack_1690991141.patch
python3 -m bin.local_search --scenario scenario/minisat/GI/train_5.txt
python3 -m bin.local_search --scenario scenario/minisat/GI/train_6.txt
python3 -m bin.local_search --scenario scenario/minisat/GI/train_7.txt
