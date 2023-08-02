from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os

EMPTY_PATCH = list()
MISSING_FILES = list()


def main(LOGS, NEXT_PHASE, BENCHMARK):
    records = ["_" for i in range(30)]

    for log in LOGS:
        file = "../_magpie_logs/{log}.log".format(log=log)
        with open(file, "r") as file:
            # check that both patch and diff file exist for this log.
            if not os.path.exists("../_magpie_logs/{log}.patch".format(log=log)) or not os.path.exists("../_magpie_logs/{log}.diff".format(log=log)):
                MISSING_FILES.append(log)
                continue

            # check for empty patch
            if os.stat("../_magpie_logs/{log}.diff".format(log=log)).st_size == 0 or os.stat("../_magpie_logs/{log}.patch".format(log=log)).st_size == 0:
                EMPTY_PATCH.append(log)
                log += " ***"
            
            # k-th, strategy, log, start time, end time, original fitness, best fitness
            row = ["_" for i in range (7)]
            
            # file name
            row[2] = log

            # start date time
            first_line = file.readline().split()
            row[3] = "{date} {time}".format(date=first_line[0], time=first_line[1][:-4:])

            for line in file:
                contents = line.split()

                if len(contents) == 3 and contents[0] == "algorithm":
                    if (contents[2] == "FirstImprovement" or contents[2] == "GeneticAlgorithm") and NEXT_PHASE != "validate":
                        print("Wrong algorithm =", log)
                        continue
                    elif contents[2] == "ValidRankingSimplify" and NEXT_PHASE != "test":
                        print("Wrong algorithm =", log)
                        continue

                # k-fold
                elif len(contents) == 5 and contents[0] == "run_cmd":
                    run_cmd = contents[4].split("_")[1][:-3]
                    row[0] = run_cmd
                
                # AC, GI, or AC + GI
                elif len(contents) == 2 and contents[0] == "possible_edits":
                    possible_edits = list()
                    for i in range(4):
                        temp_edit = file.readline().split()[0]
                        if temp_edit not in ['warmup', 'warmup_strategy', 'max_steps']:
                            possible_edits.append(temp_edit)
                    
                    if possible_edits == ["StmtReplacement", "StmtInsertion", "StmtDeletion"]:
                        row[1] = "GI"
                    elif possible_edits == ["StmtReplacement", "StmtInsertion", "StmtDeletion", "ParamSetting"]:
                        row[1] = "AC + GI"
                    elif possible_edits == ["ParamSetting"]:
                        row[1] = "AC"
                
                # retrieve best fitness
                elif (len(contents) == 6 and contents[3] == "Best" and contents[4] == "fitness:"):
                    row[6] = int(contents[5])
                
                # retrieve original fitness
                elif len(contents) == 6 and contents[2] == "[INFO]" and contents[3] == 'INITIAL' and contents[4] == 'SUCCESS':
                    row[5] = int(contents[5])

                # end date time
                elif len(contents) == 4 and contents[3] == "Diff:":
                    row[4] = "{date} {time}".format(date=contents[0], time=contents[1][:-4:])
                    break
            
            # sort into order by search strategy then by k-fold.
            if (row[1] == 'AC'):
                records[int(row[0]) - 1] = row
            elif (row[1] == 'AC + GI'):
                records[int(row[0]) + 9] = row
            else:
                records[int(row[0]) + 19] = row
    
    while ('_' in records):
        records.remove('_')

    AC_LOG    = ["_" for i in range(10)]
    GI_LOG    = ["_" for i in range(10)]
    AC_GI_LOG = ["_" for i in range(10)]

    AC_SCRIPT    = ["_" for i in range(10)]
    GI_SCRIPT    = ["_" for i in range(10)]
    AC_GI_SCRIPT = ["_" for i in range(10)]

    for record in records:
        if record[0] == '_':
            continue
        if NEXT_PHASE == "validate":
            if (record[1] == "AC"):
                    AC_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                    AC_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/{B}/AC/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(B=BENCHMARK, K=record[0], PATCH=record[2])
            elif (record[1] == "GI"):
                GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/{B}/GI/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(B=BENCHMARK, K=record[0], PATCH=record[2])
            elif (record[1] == "AC + GI"):
                AC_GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                AC_GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/{B}/AC_GI/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(B=BENCHMARK, K=record[0], PATCH=record[2])
        elif NEXT_PHASE == "test":
            if (record[1] == "AC"):
                    AC_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                    AC_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/{B}/AC/test_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(B=BENCHMARK, K=record[0], PATCH=record[2])
            elif (record[1] == "GI"):
                GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/{B}/GI/test_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(B=BENCHMARK, K=record[0], PATCH=record[2])
            elif (record[1] == "AC + GI"):
                AC_GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                AC_GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/{B}/AC_GI/test_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(B=BENCHMARK, K=record[0], PATCH=record[2])
    
    # for excel record
    np.savetxt("records.csv", records, delimiter=",", fmt='% s')

    # for graph
    np.savetxt("AC_LOG.csv", AC_LOG, delimiter=",", fmt='% s')
    np.savetxt("GI_LOG.csv", GI_LOG, delimiter=",", fmt='% s')
    np.savetxt("AC_GI_LOG.csv", AC_GI_LOG, delimiter=",", fmt='% s')

    # for validation phase. creating scripts.
    ALL_SCRIPTS = AC_SCRIPT + GI_SCRIPT + AC_GI_SCRIPT
    with open('g_all.sh','w') as file:
        for i in range(len(ALL_SCRIPTS)):
            file.write(ALL_SCRIPTS[i] + "\n")

    # with open('g1.sh','w') as file:
    #     for i in range(0, 8):
    #         file.write(ALL_SCRIPTS[i] + "\n")

    # with open('g2.sh','w') as file:
    #     for i in range(8, 16):
    #         file.write(ALL_SCRIPTS[i] + "\n")

    # with open('g3.sh','w') as file:
    #     for i in range(16, 23):
    #         file.write(ALL_SCRIPTS[i] + "\n")

    # with open('g4.sh','w') as file:
    #     for i in range(23, 30):
    #         file.write(ALL_SCRIPTS[i] + "\n")



LOGS = [
    # "minisat-hack_1690929578",
    # "minisat-hack_1690929608",
    # "minisat-hack_1690929633",
    # "minisat-hack_1690929637",
    # "minisat-hack_1690929641",
    # "minisat-hack_1690929669",
    # "minisat-hack_1690940941",
    # "minisat-hack_1690940942",
    # "minisat-hack_1690941012",
    # "minisat-hack_1690941056",
    "minisat-hack_1690989310",
    "minisat-hack_1690989316",
    "minisat-hack_1690989325",
    "minisat-hack_1690989329",
    "minisat-hack_1690989335",
    "minisat-hack_1690989341",
    "minisat-hack_1690991141",
    "minisat-hack_1690991234",
    "minisat-hack_1690991343",
    "minisat-hack_1690991652",
]

main(LOGS, NEXT_PHASE="test", BENCHMARK="minisat")

if len(EMPTY_PATCH) != 0:
    print("EMPTY patch")
    for log in EMPTY_PATCH:
        print(log)

print()
if len(MISSING_FILES) != 0:
    print("Missing files")
    for log in MISSING_FILES:
        print(log)