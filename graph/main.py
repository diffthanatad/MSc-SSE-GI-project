from datetime import datetime
import matplotlib.pyplot as plt

AC = [
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

GI = [
    "minisat-hack_1688855814",
    "minisat-hack_1688877880",
    "minisat-hack_1688974655",
    "minisat-hack_1688899950",
    "minisat-hack_1688922088",
    "minisat-hack_1688974734",
    "minisat-hack_1688855880",
    "minisat-hack_1688877877",
    "minisat-hack_1688899837",
    "minisat-hack_1688921782"
]

AC_GI = [
]
    
def grepData(file):
    LOG_FILE = "../_magpie_logs/{FILE_NAME}.log".format(FILE_NAME=file)
    with open(LOG_FILE, "r") as file:
        first_line = file.readline().split()
        start_time = datetime.strptime(first_line[0]+first_line[1][:len(first_line[1])-4:],'%Y-%m-%d%H:%M:%S')

        time = []
        fitness = []

        for line in file:
            contents = line.split()
            if len(contents) == 9 and contents[2] == "[INFO]" and contents[3].isnumeric():
                variant_time = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                timedelta = int((variant_time - start_time).total_seconds())

                time.append(timedelta)
                try:
                    fitness.append(float(contents[5]))
                except:
                    fitness.append(float(contents[5][1::]))
            elif len(contents) == 6 and contents[2] == "[INFO]" and contents[3] == "WARM":
                variant_time = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                timedelta = int((variant_time - start_time).total_seconds())

                time.append(timedelta)
                try:
                    fitness.append(float(contents[5]))
                except:
                    fitness.append(float(contents[5][1::]))

    return fitness, time

for i in range(10):
    K_TH = i+1

    GRAPH_TITLE = "Mini-SAT, First Improvement, k-{K}".format(K=K_TH)
    IMAGE_NAME = "FirstImprovement_AC_GI_k-{K}".format(K=K_TH)

    fitnesses = []
    times = []

    f, t = grepData(AC[i])
    fitnesses.append(f)
    times.append(t)

    f, t = grepData(GI[i])
    fitnesses.append(f)
    times.append(t)

    # f, t = grepData(AC_GI[i])
    # fitnesses.append(f)
    # times.append(t)

    f = plt.figure()
    f.set_figwidth(25)
    f.set_figheight(10)

    plt.plot(times[0], fitnesses[0],label = "AC")
    plt.plot(times[1], fitnesses[1], label = "GI")
    # plt.plot(time[2], fitness[2], label = "AC + GI")

    for i in range(6):
        plt.axvline(x = 3600*(1+i), color = "yellow")

    plt.xlabel('Time')
    plt.ylabel('Fitness')
    plt.title(GRAPH_TITLE)
    plt.legend()

    plt.savefig('./{FILE_NAME}.png'.format(FILE_NAME=IMAGE_NAME), bbox_inches='tight')
