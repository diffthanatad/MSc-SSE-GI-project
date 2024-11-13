from datetime import datetime
import matplotlib.pyplot as plt

AC = [
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

GI = [
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

AC_GI = [
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
    
def grepData(file, PERCENTAGE_VIEW):
    LOG_FILE = "../_magpie_logs/{FILE_NAME}.log".format(FILE_NAME=file)
    with open(LOG_FILE, "r") as file:
        first_line = file.readline().split()
        start_time = datetime.strptime(first_line[0]+first_line[1][:len(first_line[1])-4:],'%Y-%m-%d%H:%M:%S')

        time = []
        fitness = []

        for line in file:
            contents = line.split()
            if PERCENTAGE_VIEW:
                if len(contents) == 9 and contents[2] == "[INFO]" and contents[3].isnumeric():
                    variant_time = datetime.strptime(contents[0]+contents[1][:len(contents[1])-4:],'%Y-%m-%d%H:%M:%S')
                    timedelta = int((variant_time - start_time).total_seconds())

                    time.append(timedelta)
                    fitness.append(float(contents[6][1:-2:]))
            else:
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

def main(PERCENTAGE_VIEW, PROGRAM, SEARCH_STRATEGY):
    for i in range(10):
        K_TH = i+1

        if PERCENTAGE_VIEW:
            GRAPH_TITLE = "{PROGRAM}, {SEARCH_STRATEGY}, k-{K}, Percentage View".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
            IMAGE_NAME = "{PROGRAM}_{SEARCH_STRATEGY}_k-{K}_percentage_view".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
        else:
            GRAPH_TITLE = "{PROGRAM}, {SEARCH_STRATEGY}, k-{K}, fitness View".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
            IMAGE_NAME = "{PROGRAM}_{SEARCH_STRATEGY}_k-{K}_fitness_view".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
        
        fitnesses = []
        times = []

        f, t = grepData(AC[i], PERCENTAGE_VIEW)
        fitnesses.append(f)
        times.append(t)

        f, t = grepData(GI[i], PERCENTAGE_VIEW)
        fitnesses.append(f)
        times.append(t)

        f, t = grepData(AC_GI[i], PERCENTAGE_VIEW)
        fitnesses.append(f)
        times.append(t)

        f = plt.figure()
        f.set_figwidth(25)
        f.set_figheight(10)

        plt.plot(times[0], fitnesses[0],label = "AC")
        plt.plot(times[1], fitnesses[1], label = "GI")
        plt.plot(times[2], fitnesses[2], label = "AC + GI")

        for i in range(3):
            plt.axvline(x = 3600*(1+i), color = "purple")
        plt.axvline(x = 3600, color = "purple", label = "every 1 hr.")

        plt.xlabel('Time (seconds)', fontsize="20")
        if PERCENTAGE_VIEW:
            plt.ylabel('Percentage', fontsize="20")
        else:
            plt.ylabel('Fitness', fontsize="20")
        plt.title(GRAPH_TITLE, fontsize="20")
        plt.legend(fontsize="20")
        plt.grid()
        # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

        plt.xticks(fontsize="20")
        plt.yticks(fontsize="20")

        plt.savefig('./{FILE_NAME}.png'.format(FILE_NAME=IMAGE_NAME), bbox_inches='tight')

# main(
#     PERCENTAGE_VIEW = False, 
#     PROGRAM = 'Mini-SAT',
#     SEARCH_STRATEGY = 'FirstImprovement'
# )

main(
    PERCENTAGE_VIEW = True, 
    PROGRAM = 'Mini-SAT',
    SEARCH_STRATEGY = 'FirstImprovement'
)