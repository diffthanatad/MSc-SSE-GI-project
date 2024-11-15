import numpy as np
from datetime import datetime

all_patch = list()

def is_equal_number_of_edit(total_edit, AC, GI):
    return int(total_edit) == (int(AC) + int(GI))

def main(i, file_name, search_space, algorithm):
    rows = list()
    with open("../_magpie_logs/{}.log".format(file_name), "r") as file:
        first_line = file.readline().split()
        start_time = datetime.strptime(first_line[0]+first_line[1][:len(first_line[1])-4:],'%Y-%m-%d%H:%M:%S')
        
        ParamSetting = 0
        StmtInsertion = 0
        StmtDeletion = 0
        StmtReplacement = 0

        for line in file:
            if line[32:].startswith('ParamSetting') or line[32:].startswith('StmtInsertion') or line[32:].startswith('StmtDeletion') or line[32:].startswith('StmtReplacement'):
                ParamSetting = line.count('ParamSetting')
                StmtInsertion = line.count('StmtInsertion')
                StmtDeletion = line.count('StmtDeletion')
                StmtReplacement = line.count('StmtReplacement')
                continue
            if line[24:].startswith('[INFO]') and line[31:].startswith('Best patch:') and (
                line[43:].startswith('ParamSetting') or line[43:].startswith('StmtInsertion') or line[43:].startswith('StmtDeletion') or line[43:].startswith('StmtReplacement')
            ):
                ParamSetting = line.count('ParamSetting')
                StmtInsertion = line.count('StmtInsertion')
                StmtDeletion = line.count('StmtDeletion')
                StmtReplacement = line.count('StmtReplacement')
                all_patch.append([algorithm, search_space, i, (ParamSetting + StmtInsertion + StmtDeletion + StmtReplacement),ParamSetting, StmtInsertion, StmtDeletion, StmtReplacement, rows[-1][0]])
                break
            
            contents = line.split()
            if len(contents) == 6 and contents[3] == "INITIAL" and contents[4] == "SUCCESS":
                """ Initial Success """
                variant_number = -1
                timestamp = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                time_elapsed = 0
                status = "INITIAL SUCCESS"
                fitness = int(contents[5])
                percent = 100
                edits = 0

                rows.append([variant_number, timestamp, time_elapsed, status, fitness, percent, edits, 0, 0, 0, 0])
            elif len(contents) == 9 and contents[2] == "[INFO]" and contents[4] == "SUCCESS":
                """ Success """
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
                
                if not is_equal_number_of_edit(edits, ParamSetting, (StmtInsertion + StmtDeletion + StmtReplacement)):
                    print("NOT EQUAL:", contents)
                    print(edits, '|', ParamSetting, StmtInsertion, StmtDeletion, StmtReplacement)
                    exit(0)
                
                rows.append([variant_number, timestamp, time_elapsed, status, fitness, percent, edits, ParamSetting, StmtInsertion, StmtDeletion, StmtReplacement])
                ParamSetting = 0
                StmtInsertion = 0
                StmtDeletion = 0
                StmtReplacement = 0
            elif len(contents) == 8 and contents[2] == "[INFO]" and contents[3] != "Best" and contents[4] != "patch:":
                """ Error """
                variant_number = contents[3]                
                timestamp = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                time_elapsed = int((timestamp - start_time).total_seconds())
                status = contents[4]
                fitness = None
                percent = None
                edits = contents[6][1:]

                if not is_equal_number_of_edit(edits, ParamSetting, (StmtInsertion + StmtDeletion + StmtReplacement)):
                    print("NOT EQUAL:", contents)
                    print(edits, '|', ParamSetting, StmtInsertion, StmtDeletion, StmtReplacement)
                    exit(0)
                
                rows.append([variant_number, timestamp, time_elapsed, status, fitness, percent, edits, ParamSetting, StmtInsertion, StmtDeletion, StmtReplacement])
                ParamSetting = 0
                StmtInsertion = 0
                StmtDeletion = 0
                StmtReplacement = 0
    
    np.savetxt("../results/{}_{}_{}.csv".format(algorithm, search_space, i), rows, delimiter=",", fmt='% s', header="variant_number,timestamp,time_elapse,status,fitness,percentage,edit,ParamSetting,StmtInsertion,StmtDeletion,StmtReplacement", comments='')

# main(1, "minisat-hack_1691145361", "ac-gi", "ga")
# print(all_patch)

def minisat():
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

    """ Genetic Algorithm 100 population size """
    ga_ac_logs = [
        "minisat-hack_1692371461",
        "minisat-hack_1692382819",
        "minisat-hack_1692394207",
        "minisat-hack_1692405859",
        "minisat-hack_1692417279",
        "minisat-hack_1692371462",
        "minisat-hack_1692382794",
        "minisat-hack_1692394183",
        "minisat-hack_1692405812",
        "minisat-hack_1692417149",
    ]
    for i in range(10):
        main(i+1, ga_ac_logs[i], "ac", "ga100")

    ga_ac_gi_logs = [
        "minisat-hack_1692371463",
        "minisat-hack_1692382852",
        "minisat-hack_1692394265",
        "minisat-hack_1692405876",
        "minisat-hack_1692417306",
        "minisat-hack_1692429365",
        "minisat-hack_1692440722",
        "minisat-hack_1692452066",
        "minisat-hack_1692463410",
        "minisat-hack_1692474735",
    ]
    for i in range(10):
        main(i+1, ga_ac_gi_logs[i], "ac-gi", "ga100")

    ga_gi_logs = [
        "minisat-hack_1692429363",
        "minisat-hack_1692440755",
        "minisat-hack_1692452100",
        "minisat-hack_1692463509",
        "minisat-hack_1692474881",
        "minisat-hack_1692429364",
        "minisat-hack_1692440705",
        "minisat-hack_1692452058",
        "minisat-hack_1692463407",
        "minisat-hack_1692474732",
    ]
    for i in range(10):
        main(i+1, ga_gi_logs[i], "gi", "ga100")

    np.savetxt("../results/edit_analysis.csv", all_patch, delimiter=",", fmt='% s', header="algorithm,search_space,k_th,edit,ParamSetting,StmtInsertion,StmtDeletion,StmtReplacement,gen", comments='')

def sat4j():
    """ Local Search """
    ls_ac_logs = [
        "sat4j_1692522821",
        "sat4j_1692522828",
        "sat4j_1692522829",
        "sat4j_1692522822",
        "sat4j_1692540896",
        "sat4j_1692540893",
        "sat4j_1692540895",
        "sat4j_1692540894",
        "sat4j_1692559033",
        "sat4j_1692559032",
    ]
    for i in range(10):
        main(i+1, ls_ac_logs[i], "ac", "ls")

    ls_ac_gi_logs = [
        "sat4j_1692559034",
        "sat4j_1692559031",
        "sat4j_1692559390",
        "sat4j_1692577068",
        "sat4j_1692577069",
        "sat4j_1692577070",
        "sat4j_1692577407",
        "sat4j_1692595104",
        "sat4j_1692595280",
        "sat4j_1692633725",
    ]
    for i in range(10):
        main(i+1, ls_ac_gi_logs[i], "ac-gi", "ls")

    ls_gi_logs = [
        "sat4j_1692595626",
        "sat4j_1692595627",
        "sat4j_1692613289",
        "sat4j_1692613457",
        "sat4j_1692613805",
        "sat4j_1692613804",
        "sat4j_1692614145",
        "sat4j_1692631369",
        "sat4j_1692631556",
    ]
    for i in range(9):
        main(i+1, ls_gi_logs[i], "gi", "ls")
    
    np.savetxt("../results-sat4j/edit_analysis.csv", all_patch, delimiter=",", fmt='% s', header="algorithm,search_space,k_th,edit,ParamSetting,StmtInsertion,StmtDeletion,StmtReplacement,gen", comments='')
    
minisat()
# sat4j()