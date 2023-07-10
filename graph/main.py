import numpy as np
import matplotlib.pyplot as plt

LOGS = [
    "minisat-hack_1688855807",
    "minisat-hack_1688877840",
    "minisat-hack_1688899802",
    "minisat-hack_1688921946",
    "minisat-hack_1688944149",
    "minisat-hack_1688855811",
    "minisat-hack_1688877857",
    "minisat-hack_1688899846",
    "minisat-hack_1688921807",
    "minisat-hack_1688943760"
]

HR = [
    [117,   279,    413,    556,    749,    922],
    [226,   505,    804,    1111,   1395,   1697],
    [107,   230,    395,    528,    702,    872],
    [82,    179,    271,    366,    470,    575],
    [255,   666,    1182,   1629,   2025,   2363],
    [167,   380,    616,    789,    948,    1141],
    [240,   496,    797,    1118,   1434,   1756],
    [243,   526,    910,    1244,   1585,   1995],
    [338,   752,    1283,   1786,   2330,   2823],
    [129,   311,    411,    516,    655,    833]
]

for i in range(10):
    I_TH = i + 1
    GRAPH_TITLE = "Mini-SAT, First Improvement, AC, k-{K}".format(K=I_TH)
    IMAGE_NAME = "FirstImprovement_AC_k-{K}".format(K=I_TH)

    LOG_FILE = "../_magpie_logs/{FILE_NAME}.log".format(FILE_NAME=LOGS[i])
    colour = ['r', 'g', 'black', 'purple', 'orange', 'yellow']
    label = ['1 hr.', '2 hr.', '3 hr.', '4 hr.', '5 hr.', '6 hr.']
    variants = []
    fitness = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            contents = line.split()
            if len(contents) == 9 and contents[2] == "[INFO]" and contents[3].isnumeric():
                variants.append(int(contents[3]))
                try:
                    fitness.append(float(contents[5]))
                except:
                    fitness.append(float(contents[5][1::]))

    f = plt.figure()
    f.set_figwidth(30)
    f.set_figheight(10)

    plt.plot(variants, fitness)
    plt.xlabel('Variant')
    plt.ylabel('Fitness')
    plt.title(GRAPH_TITLE)

    for j in range(6):
        plt.axvline(x = HR[i][j], color = colour[j], label = label[j])

    plt.xticks(np.arange(min(variants), max(variants), 45))
    plt.legend()
    plt.savefig('./{FILE_NAME}.png'.format(FILE_NAME=IMAGE_NAME), bbox_inches='tight')
