from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

LOGS = [
    "../_magpie_logs/minisat-hack_1689188416.log",
    "../_magpie_logs/minisat-hack_1689188420.log",
    "../_magpie_logs/minisat-hack_1689188424.log",
    "../_magpie_logs/minisat-hack_1689188428.log",
    "../_magpie_logs/minisat-hack_1689201742.log",
    "../_magpie_logs/minisat-hack_1689201795.log",
    "../_magpie_logs/minisat-hack_1689201810.log",
    "../_magpie_logs/minisat-hack_1689202003.log",
    "../_magpie_logs/minisat-hack_1689215148.log",
    "../_magpie_logs/minisat-hack_1689215149.log",
    "../_magpie_logs/minisat-hack_1689215282.log",
    "../_magpie_logs/minisat-hack_1689215372.log",
    "../_magpie_logs/minisat-hack_1689228494.log",
    "../_magpie_logs/minisat-hack_1689228688.log",
    "../_magpie_logs/minisat-hack_1689228744.log",
    "../_magpie_logs/minisat-hack_1689228780.log",
    "../_magpie_logs/minisat-hack_1689242037.log",
    "../_magpie_logs/minisat-hack_1689242075.log",
    "../_magpie_logs/minisat-hack_1689242165.log",
    "../_magpie_logs/minisat-hack_1689242285.log",
    "../_magpie_logs/minisat-hack_1689255471.log",
    "../_magpie_logs/minisat-hack_1689255510.log",
    "../_magpie_logs/minisat-hack_1689255626.log",
    "../_magpie_logs/minisat-hack_1689255655.log",
    "../_magpie_logs/minisat-hack_1689268835.log",
    "../_magpie_logs/minisat-hack_1689269074.log",
    "../_magpie_logs/minisat-hack_1689269204.log",
    "../_magpie_logs/minisat-hack_1689280650.log",
    "../_magpie_logs/minisat-hack_1689282465.log",
    "../_magpie_logs/minisat-hack_1689282573.log",
]

records = list()
for log in LOGS:
    with open(log, "r") as file:
        temp = list()
        temp.append(log[16:-4:])

        first_line = file.readline().split()
        temp.append("{date} {time}".format(date=first_line[0], time=first_line[1][:-4:]))

        for line in file:
            contents = line.split()
            if len(contents) == 5 and contents[0] == "run_cmd":
                run_cmd = contents[4].split("_")[1][:-3]
                temp.append(run_cmd)
            if len(contents) == 2 and contents[0] == "possible_edits":
                possible_edits = list()
                for i in range(4):
                    temp_edit = file.readline().split()[0]
                    if temp_edit not in ['warmup', 'warmup_strategy', 'max_steps']:
                        possible_edits.append(temp_edit)
                
                if possible_edits == ["StmtReplacement", "StmtInsertion", "StmtDeletion"]:
                    temp.append("GI")
                elif possible_edits == ["StmtReplacement", "StmtInsertion", "StmtDeletion", "ParamSetting"]:
                    temp.append("AC + GI")
                elif possible_edits == ["ParamSetting"]:
                    temp.append("AC")
                break
        records.append(temp)

AC_LOG = [0 for i in range(10)]
GI_LOG = [0 for i in range(10)]
AC_GI_LOG = [0 for i in range(10)]

AC_SCRIPT = [0 for i in range(10)]
GI_SCRIPT = [0 for i in range(10)]
AC_GI_SCRIPT = [0 for i in range(10)]

for record in records:
    if (record[3] == "AC"):
        AC_LOG[int(record[2]) - 1] = "'{file}.log',".format(file=record[0])
        AC_SCRIPT[int(record[2]) - 1] = "/usr/local/bin/python3.10 -m bin.minify_patch --scenario scenario/AC/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[2], PATCH=record[0])
    elif (record[3] == "GI"):
        GI_LOG[int(record[2]) - 1] = "'{file}.log',".format(file=record[0])
        GI_SCRIPT[int(record[2]) - 1] = "/usr/local/bin/python3.10 -m bin.minify_patch --scenario scenario/GI/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[2], PATCH=record[0])
    elif (record[3] == "AC + GI"):
        AC_GI_LOG[int(record[2]) - 1] = "'{file}.log',".format(file=record[0])
        AC_GI_SCRIPT[int(record[2]) - 1] = "/usr/local/bin/python3.10 -m bin.minify_patch --scenario scenario/AC_GI/validate_{K}.txt --patch _magpie_logs/{PATCH}.patch".format(K=record[2], PATCH=record[0])

# for excel record
np.savetxt("records.csv", records, delimiter=", ", fmt='% s')       

# for graph
np.savetxt("AC_LOG.csv", AC_LOG, delimiter=", ", fmt='% s')         
np.savetxt("GI_LOG.csv", GI_LOG, delimiter=", ", fmt='% s')
np.savetxt("AC_GI_LOG.csv", AC_GI_LOG, delimiter=", ", fmt='% s')

# for validation phase. creating scripts.
ALL_SCRIPTS = AC_SCRIPT + GI_SCRIPT + AC_GI_SCRIPT
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