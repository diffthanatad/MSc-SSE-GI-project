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
        
        # k-th, strategy, log, start time, end time, original fitness, best fitness
        row = ["_" for i in range (7)]

        with open(file, "r") as file:
            # check that both patch and diff file exist for this log.
            if not os.path.exists("../_magpie_logs/{log}.patch".format(log=log)) or not os.path.exists("../_magpie_logs/{log}.diff".format(log=log)):
                MISSING_FILES.append(log)
                # continue

            # check for empty patch
            try:
                if os.stat("../_magpie_logs/{log}.diff".format(log=log)).st_size == 0 or os.stat("../_magpie_logs/{log}.patch".format(log=log)).st_size == 0:
                    EMPTY_PATCH.append(log)
                    log += " ***"
            except:
                pass
            
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
                elif len(contents) == 6 and contents[2] == "[INFO]" and contents[3] == "Log" and contents[4] == "file:":
                    row[4] = "{date} {time}".format(date=contents[0], time=contents[1][:-4:])
            
            # sort into order by search strategy then by k-fold.
            if (row[1] == 'AC'):
                records[int(row[0]) - 1] = row
            elif (row[1] == 'AC + GI'):
                records[int(row[0]) + 9] = row
            else:
                records[int(row[0]) + 19] = row
    
    # for i in records:
    #     print(i)

    for i in range(30):
        if records[i] == "_":
            records[i] = ["_" for i in range (7)]
    
    # while ('_' in records):
    #     records.remove('_')

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
    ALL_SCRIPTS = AC_SCRIPT + AC_GI_SCRIPT + GI_SCRIPT 
    with open('g_all.sh','w') as file:
        for i in range(len(ALL_SCRIPTS)):
            file.write(ALL_SCRIPTS[i] + "\n")
    
    with open('patch_ac.txt', 'w') as file:
        for i in range(10):
            file.write("_magpie_logs/{}.patch\n".format(AC_LOG[i][1:-6:]))
    
    with open('patch_ac_gi.txt', 'w') as file:
        for i in range(10):
            file.write("_magpie_logs/{}.patch\n".format(AC_GI_LOG[i][1:-6:]))
    
    with open('patch_gi.txt', 'w') as file:
        for i in range(10):
            file.write("_magpie_logs/{}.patch\n".format(GI_LOG[i][1:-6:]))

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
    # "minisat-hack_1690929578", ## Minisat FirstImprovement Train
    # "minisat-hack_1690929608",
    # "minisat-hack_1690929633",
    # "minisat-hack_1690929637",
    # "minisat-hack_1690929641",
    # "minisat-hack_1690929669",
    # "minisat-hack_1690940941",
    # "minisat-hack_1690940942",
    # "minisat-hack_1690941012",
    # "minisat-hack_1690941056",
    # "minisat-hack_1691009877",
    # "minisat-hack_1691009891",
    # "minisat-hack_1691009894",
    # "minisat-hack_1691009898",
    # "minisat-hack_1691009902",
    # "minisat-hack_1691018823",
    # "minisat-hack_1691021225",
    # "minisat-hack_1691021233",
    # "minisat-hack_1691021236",
    # "minisat-hack_1691021245",
    # "minisat-hack_1691021277",
    # "minisat-hack_1691030213",
    # "minisat-hack_1691032545",
    # "minisat-hack_1691032560",
    # "minisat-hack_1691032564",
    # "minisat-hack_1691032583",
    # "minisat-hack_1691032620",
    # "minisat-hack_1691041556",
    # "minisat-hack_1691043918",
    # "minisat-hack_1691043948",

    # "minisat-hack_1690989310", ## Minisat FirstImprovement Validate
    # "minisat-hack_1690989316",
    # "minisat-hack_1690989325",
    # "minisat-hack_1690989329",
    # "minisat-hack_1690989335",
    # "minisat-hack_1690989341",
    # "minisat-hack_1690991141",
    # "minisat-hack_1690991234",
    # "minisat-hack_1690991343",
    # "minisat-hack_1690991652",
    # "minisat-hack_1691061439",
    # "minisat-hack_1691061443",
    # "minisat-hack_1691061458",
    # "minisat-hack_1691061462",
    # "minisat-hack_1691061466",
    # "minisat-hack_1691061469",
    # "minisat-hack_1691063518",
    # "minisat-hack_1691063519",
    # "minisat-hack_1691063658",
    # "minisat-hack_1691063752",
    # "minisat-hack_1691064063",
    # "minisat-hack_1691064153",
    # "minisat-hack_1691065598",
    # "minisat-hack_1691065648",
    # "minisat-hack_1691065827",
    # "minisat-hack_1691065828",
    # "minisat-hack_1691065970",
    # "minisat-hack_1691066447",
    # "minisat-hack_1691067083",
    # "minisat-hack_1691067179",

    # "minisat-hack_1691080228", ## Minisat FirstImprovement Test
    # "minisat-hack_1691080293",
    # "minisat-hack_1691080391",
    # "minisat-hack_1691080497",
    # "minisat-hack_1691080555",
    # "minisat-hack_1691080607",
    # "minisat-hack_1691089649",
    # "minisat-hack_1691090021",
    # "minisat-hack_1691090256",
    # "minisat-hack_1691090541",
    # "minisat-hack_1691090562",
    # "minisat-hack_1691090930",
    # "minisat-hack_1691099334",
    # "minisat-hack_1691099942",
    # "minisat-hack_1691100036",

    # "minisat-hack_1691133962", ## Minisat GeneticAlgorithm Train
    # "minisat-hack_1691133979",
    # "minisat-hack_1691133995",
    # "minisat-hack_1691134014",
    # "minisat-hack_1691134031",
    # "minisat-hack_1691134045",
    # "minisat-hack_1691145311",
    # "minisat-hack_1691145321",
    # "minisat-hack_1691145361",
    # "minisat-hack_1691145365",
    # "minisat-hack_1691145378",
    # "minisat-hack_1691145439",
    # "minisat-hack_1691156638",
    # "minisat-hack_1691156684",
    # "minisat-hack_1691156713",
    # "minisat-hack_1691156724",
    # "minisat-hack_1691156730",
    # "minisat-hack_1691156771",
    # "minisat-hack_1691167978",
    # "minisat-hack_1691168050",
    # "minisat-hack_1691168069",
    # "minisat-hack_1691179300",
    # "minisat-hack_1691179373",
    # "minisat-hack_1691179403",
    # "minisat-hack_1691179664",
    # "minisat-hack_1691179692",
    # "minisat-hack_1691179737",
    # "minisat-hack_1691221367",
    # "minisat-hack_1691221371",
    # "minisat-hack_1691221374",

    # "minisat-hack_1691241709",  ## Minisat GeneticAlgorithm Validate
    # "minisat-hack_1691241722",
    # "minisat-hack_1691241747",
    # "minisat-hack_1691241757",
    # "minisat-hack_1691241765",
    # "minisat-hack_1691241773",
    # "minisat-hack_1691243717",
    # "minisat-hack_1691243823",
    # "minisat-hack_1691243828",
    # "minisat-hack_1691244018",
    # "minisat-hack_1691244020",
    # "minisat-hack_1691244172",
    # "minisat-hack_1691245856",
    # "minisat-hack_1691245938",
    # "minisat-hack_1691246082",
    # "minisat-hack_1691246140",
    # "minisat-hack_1691246143",
    # "minisat-hack_1691246190",
    # "minisat-hack_1691247867",
    # "minisat-hack_1691248034",
    # "minisat-hack_1691248118",
    # "minisat-hack_1691248257",
    # "minisat-hack_1691248333",
    # "minisat-hack_1691248597",
    # "minisat-hack_1691249887",
    # "minisat-hack_1691250331",
    # "minisat-hack_1691250344",
    # "minisat-hack_1691250472",
    # "minisat-hack_1691250703",
    # "minisat-hack_1691251050",

    # "minisat-hack_1691255851", ## Minisat GeneticAlgorithm Test
    # "minisat-hack_1691255867",
    # "minisat-hack_1691255910",
    # "minisat-hack_1691255940",
    # "minisat-hack_1691255970",
    # "minisat-hack_1691255987",
    # "minisat-hack_1691265339",
    # "minisat-hack_1691265738",
    # "minisat-hack_1691266039",
    # "minisat-hack_1691266148",
    # "minisat-hack_1691266267",
    # "minisat-hack_1691266282",
    # "minisat-hack_1691276070",
    # "minisat-hack_1691276273",
    # "minisat-hack_1691276371",
    # "minisat-hack_1691276588",

    "minisat-hack_1692371461", ## GeneticAlgorithm (100 pop) Train
    "minisat-hack_1692371462",
    "minisat-hack_1692371463",
    "minisat-hack_1692382794",
    "minisat-hack_1692382819",
    "minisat-hack_1692382852",
    "minisat-hack_1692394183",
    "minisat-hack_1692394207",
    "minisat-hack_1692394265",
    "minisat-hack_1692405812",
    "minisat-hack_1692405859",
    "minisat-hack_1692405876",
    "minisat-hack_1692417149",
    "minisat-hack_1692417279",
    "minisat-hack_1692417306",
    "minisat-hack_1692429363",
    "minisat-hack_1692429364",
    "minisat-hack_1692429365",
    "minisat-hack_1692440705",
    "minisat-hack_1692440722",
    "minisat-hack_1692440755",
    "minisat-hack_1692452058",
    "minisat-hack_1692452066",
    "minisat-hack_1692452100",
    "minisat-hack_1692463407",
    "minisat-hack_1692463410",
    "minisat-hack_1692463509",
    "minisat-hack_1692474732",
    "minisat-hack_1692474735",
    "minisat-hack_1692474881",

    "minisat-hack_1692606990", ## GeneticAlgorithm (100 pop) Validate
    "minisat-hack_1692606991",
    "minisat-hack_1692606992",
    "minisat-hack_1692609035",
    "minisat-hack_1692609155",
    "minisat-hack_1692609376",
    "minisat-hack_1692611220",
    "minisat-hack_1692611221",
    "minisat-hack_1692611498",
    "minisat-hack_1692613161",
    "minisat-hack_1692613302",
    "minisat-hack_1692613457",
    "minisat-hack_1692615055",
    "minisat-hack_1692615169",
    "minisat-hack_1692615326",
    "minisat-hack_1692617047",
    "minisat-hack_1692617226",
    "minisat-hack_1692617955",
    "minisat-hack_1692618941",
    "minisat-hack_1692619183",
    "minisat-hack_1692619831",
    "minisat-hack_1692620962",
    "minisat-hack_1692621490",
    "minisat-hack_1692622450",
    "minisat-hack_1692622713",
    "minisat-hack_1692623780",
    "minisat-hack_1692623866",
    "minisat-hack_1692624637",
    "minisat-hack_1692625555",
    "minisat-hack_1692626504",

    # "sat4j_1692313299", ## sat4j FirstImprovement Train
    # "sat4j_1692313300",
    # "sat4j_1692313310",
    # "sat4j_1692313311",
    # "sat4j_1692313841",
    # "sat4j_1692331630",
    # "sat4j_1692331631",
    # "sat4j_1692331818",
    # "sat4j_1692332172",
    # "sat4j_1692349947",
    # "sat4j_1692350134",
    # "sat4j_1692350135",
    # "sat4j_1692350136",
    # "sat4j_1692350858",
    # "sat4j_1692368168",
    # "sat4j_1692368311",
    # "sat4j_1692368312",
    # "sat4j_1692369169",
    # "sat4j_1692386287",
    # "sat4j_1692386461",
    # "sat4j_1692386462",
    # "sat4j_1692387004",
    # "sat4j_1692387312",
    # "sat4j_1692387681",
    # "sat4j_1692388212",
    # "sat4j_1692404458",
    # "sat4j_1692404810",
    # "sat4j_1692405164",
    # "sat4j_1692406431",
    # "sat4j_1692422627",
    # "sat4j_1692422992",
    # "sat4j_1692422993",
    # "sat4j_1692423347",
    # "sat4j_1692424608",
    # "sat4j_1692430908",
    # "sat4j_1692431268",
    # "sat4j_1692441038",
    # "sat4j_1692441217",
    # "sat4j_1692441584",
    # "sat4j_1692459229",

    "sat4j_1692482842", ## sat4j FirstImprovement Validate
    "sat4j_1692482843",
    "sat4j_1692482844",
    "sat4j_1692482845",
    "sat4j_1692486395",
    "sat4j_1692486396",
    "sat4j_1692486578",
    "sat4j_1692486754",
    "sat4j_1692490079",
    "sat4j_1692490247",
    "sat4j_1692490248",
    "sat4j_1692490495",
    "sat4j_1692493672",
    "sat4j_1692493673",
    "sat4j_1692494035",
    "sat4j_1692494395",
    "sat4j_1692497281",
    "sat4j_1692497450",
    "sat4j_1692497800",
    "sat4j_1692497801",
    "sat4j_1692500867",
    "sat4j_1692501404",
    "sat4j_1692501586",
    "sat4j_1692501587",
    "sat4j_1692504289",
    "sat4j_1692504828",
    "sat4j_1692505012",
    "sat4j_1692505362",
    "sat4j_1692508069",
]

main(LOGS, NEXT_PHASE="test", BENCHMARK="sat4j")

if len(EMPTY_PATCH) != 0:
    print("EMPTY patch")
    for log in EMPTY_PATCH:
        print(log)

print()
if len(MISSING_FILES) != 0:
    print("Missing files")
    for log in MISSING_FILES:
        print(log)