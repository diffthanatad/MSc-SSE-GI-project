python3 -m bin.revalidate_patch --scenario scenario/minisat/AC/test_5.txt --patch _magpie_logs/minisat-hack_1690989335.patch
python3 -m bin.local_search --scenario scenario/minisat/GI/train_2.txt
python3 -m bin.local_search --scenario scenario/minisat/GI/train_3.txt
python3 -m bin.local_search --scenario scenario/minisat/GI/train_4.txt
