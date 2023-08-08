import numpy as np
from datetime import datetime

def main(i, file_name, search_space, algorithm):
    rows = list()
    with open("../_magpie_logs/{}.log".format(file_name), "r") as file:
        first_line = file.readline().split()
        start_time = datetime.strptime(first_line[0]+first_line[1][:len(first_line[1])-4:],'%Y-%m-%d%H:%M:%S')

        for line in file:
            contents = line.split()

            if len(contents) == 6 and contents[3] == "INITIAL" and contents[4] == "SUCCESS":
                variant_number = -1
                timestamp = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                time_elapsed = int((timestamp - start_time).total_seconds())
                status = "INITIAL SUCCESS"
                fitness = int(contents[5])
                percent = 100
                edits = 0
                rows.append([variant_number, timestamp, time_elapsed, status, fitness, percent, edits])
            elif len(contents) == 9 and contents[2] == "[INFO]" and contents[4] == "SUCCESS":
                variant_number = contents[3]                
                timestamp = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                time_elapsed = int((timestamp - start_time).total_seconds())
                status = contents[4]
                if contents[5][0] == "*":
                    fitness = int(contents[5][1:])
                else:
                    fitness = int(contents[5])
                percent = float(contents[6][1:-2:])
                edits = contents[7][1:]
                rows.append([variant_number, timestamp, time_elapsed, status, fitness, percent, edits])
            elif len(contents) == 8 and contents[2] == "[INFO]":
                variant_number = contents[3]                
                timestamp = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                time_elapsed = int((timestamp - start_time).total_seconds())
                status = contents[4]
                fitness = None
                percent = None
                edits = None
                rows.append([variant_number, timestamp, time_elapsed, status, fitness, percent, edits])
    np.savetxt("../results/{}_{}_{}.csv".format(algorithm, search_space, i), rows, delimiter=",", fmt='% s', header="variant number, timestamp, time elapse, status, fitness, percentage, edit",)

""" Genetic Algorithm """
ga_ac_logs = [
    "minisat-hack_1691133962",
    "minisat-hack_1691145321",
    "minisat-hack_1691156684",
    "minisat-hack_1691221371",
    "minisat-hack_1691179664",
    "minisat-hack_1691133979",
    "minisat-hack_1691145311",
    "minisat-hack_1691156638",
    "minisat-hack_1691167978",
    "minisat-hack_1691179300",
]
for i in range(10):
    main(i+1, ga_ac_logs[i], "ac", "ga")

ga_ac_gi_logs = [
    "minisat-hack_1691133995",
    "minisat-hack_1691145361",
    "minisat-hack_1691156730",
    "minisat-hack_1691221374",
    "minisat-hack_1691179692",
    "minisat-hack_1691134014",
    "minisat-hack_1691145365",
    "minisat-hack_1691156724",
    "minisat-hack_1691168069",
    "minisat-hack_1691179403",
]
for i in range(10):
    main(i+1, ga_ac_gi_logs[i], "ac-gi", "ga")

ga_gi_logs = [
    "minisat-hack_1691134031",
    "minisat-hack_1691145439",
    "minisat-hack_1691156771",
    "minisat-hack_1691221367",
    "minisat-hack_1691179737",
    "minisat-hack_1691134045",
    "minisat-hack_1691145378",
    "minisat-hack_1691156713",
    "minisat-hack_1691168050",
    "minisat-hack_1691179373",
]
for i in range(10):
    main(i+1, ga_gi_logs[i], "gi", "ga")

""" Local Search """
ls_ac_logs = [
    "minisat-hack_1690929578",
    "minisat-hack_1690929608",
    "minisat-hack_1690929633",
    "minisat-hack_1690929637",
    "minisat-hack_1690929641",
    "minisat-hack_1690929669",
    "minisat-hack_1690940941",
    "minisat-hack_1690940942",
    "minisat-hack_1690941012",
    "minisat-hack_1690941056",
]
for i in range(10):
    main(i+1, ls_ac_logs[i], "ac", "ls")

ls_ac_gi_logs = [
    "minisat-hack_1691018823",
    "minisat-hack_1691030213",
    "minisat-hack_1691041556",
    "minisat-hack_1691009877",
    "minisat-hack_1691021277",
    "minisat-hack_1691032620",
    "minisat-hack_1691043948",
    "minisat-hack_1691009894",
    "minisat-hack_1691021225",
    "minisat-hack_1691032545",
]
for i in range(10):
    main(i+1, ls_ac_gi_logs[i], "ac-gi", "ls")

ls_gi_logs = [
    "minisat-hack_1691043918",
    "minisat-hack_1691009891",
    "minisat-hack_1691021233",
    "minisat-hack_1691032583",
    "minisat-hack_1691009902",
    "minisat-hack_1691021236",
    "minisat-hack_1691032560",
    "minisat-hack_1691009898",
    "minisat-hack_1691021245",
    "minisat-hack_1691032564",
]
for i in range(10):
    main(i+1, ls_gi_logs[i], "gi", "ls")