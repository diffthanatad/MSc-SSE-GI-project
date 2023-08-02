from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os

def main(LOGS, NEXT_PHASE):
    records = list()
    for log in LOGS:
        file = "../_magpie_logs/{log}.log".format(log=log)
        with open(file, "r") as file:
            # check that both patch and diff file exist for this log.
            if not os.path.exists("../_magpie_logs/{log}.patch".format(log=log)) or not os.path.exists("../_magpie_logs/{log}.diff".format(log=log)):
                print("Does not exist for =", log)
                continue
            if os.stat("../_magpie_logs/{log}.diff".format(log=log)).st_size == 0 or os.stat("../_magpie_logs/{log}.patch".format(log=log)).st_size == 0:
                log += " ***"
                print("Empty =", log)

            # file name
            row = ["_" for i in range (4)]
            row[2] = log

            # date time
            first_line = file.readline().split()
            row[3] = "{date} {time}".format(date=first_line[0], time=first_line[1][:-4:])

            for line in file:
                contents = line.split()

                if len(contents) == 3 and contents[0] == "algorithm":
                    # print(contents)
                    if contents[2] == "FirstImprovement" and NEXT_PHASE != "validate":
                        print("Wrong algorithm =", log)
                        continue
                    elif contents[2] == "ValidRankingSimplify" and NEXT_PHASE != "test":
                        print("Wrong algorithm =", log)
                        continue

                # k-fold
                if len(contents) == 5 and contents[0] == "run_cmd":
                    run_cmd = contents[4].split("_")[1][:-3]
                    row[0] = run_cmd
                
                # AC, GI, or AC + GI
                if len(contents) == 2 and contents[0] == "possible_edits":
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
                    break
            records.append(row)

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
                AC_SCRIPT[int(record[0]) - 1] = "python3 -m bin.minify_patch --scenario scenario/AC/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[0], PATCH=record[2])
            elif (record[1] == "GI"):
                GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.minify_patch --scenario scenario/GI/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[0], PATCH=record[2])
            elif (record[1] == "AC + GI"):
                AC_GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                AC_GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.minify_patch --scenario scenario/AC_GI/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[0], PATCH=record[2])
        elif NEXT_PHASE == "test":
            if (record[1] == "AC"):
                AC_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                AC_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/AC/test.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[0], PATCH=record[2])
            elif (record[1] == "GI"):
                GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/GI/test.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[0], PATCH=record[2])
            elif (record[1] == "AC + GI"):
                AC_GI_LOG[int(record[0]) - 1] = "'{file}.log',".format(file=record[2])
                AC_GI_SCRIPT[int(record[0]) - 1] = "python3 -m bin.revalidate_patch --scenario scenario/AC_GI/test.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[0], PATCH=record[2])
        
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

    with open('g1.sh','w') as file:
        for i in range(0, 8):
            file.write(ALL_SCRIPTS[i] + "\n")

    with open('g2.sh','w') as file:
        for i in range(8, 16):
            file.write(ALL_SCRIPTS[i] + "\n")

    with open('g3.sh','w') as file:
        for i in range(16, 23):
            file.write(ALL_SCRIPTS[i] + "\n")

    with open('g4.sh','w') as file:
        for i in range(23, 30):
            file.write(ALL_SCRIPTS[i] + "\n")

LOGS = [
    "minisat-hack_1689337310",
    "minisat-hack_1689337311",
    "minisat-hack_1689337313",
    "minisat-hack_1689337315",
    "minisat-hack_1689346449",
    "minisat-hack_1689354186",
    "minisat-hack_1689354375",
    "minisat-hack_1689356831",
    "minisat-hack_1689362139",
    "minisat-hack_1689367511",
    "minisat-hack_1689369373",
    "minisat-hack_1689372417",
    "minisat-hack_1689376850",
    "minisat-hack_1689380258",
    "minisat-hack_1689385026",
    "minisat-hack_1689385512",
    "minisat-hack_1689387799",
    "minisat-hack_1689389655",
    "minisat-hack_1689398363",
    "minisat-hack_1689399178",
    "minisat-hack_1689403051",
    "minisat-hack_1689409645",
    "minisat-hack_1689414513",
    "minisat-hack_1689418001",
    "minisat-hack_1689420863",
    "minisat-hack_1689430900",
    "minisat-hack_1689435082",
    "minisat-hack_1689444628",
    "minisat-hack_1689451548",
    "minisat-hack_1689462349",
]

main(LOGS, NEXT_PHASE="test")