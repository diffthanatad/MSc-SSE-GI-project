from datetime import datetime
import matplotlib.pyplot as plt

AC = [
    'minisat-hack_1689242037',
    'minisat-hack_1689255471',
    'minisat-hack_1689280650',
    'minisat-hack_1689188428',
    'minisat-hack_1689202003',
    'minisat-hack_1689215372',
    'minisat-hack_1689228780',
    'minisat-hack_1689242165',
    'minisat-hack_1689255510',
    'minisat-hack_1689268835',
]

GI = [
    'minisat-hack_1689215282',
    'minisat-hack_1689228744',
    'minisat-hack_1689242075',
    'minisat-hack_1689255626',
    'minisat-hack_1689269204',
    'minisat-hack_1689282573',
    'minisat-hack_1689188424',
    'minisat-hack_1689201795',
    'minisat-hack_1689215148',
    'minisat-hack_1689228494',
]

AC_GI = [
    'minisat-hack_1689188416',
    'minisat-hack_1689201810',
    'minisat-hack_1689215149',
    'minisat-hack_1689228688',
    'minisat-hack_1689242285',
    'minisat-hack_1689255655',
    'minisat-hack_1689269074',
    'minisat-hack_1689282465',
    'minisat-hack_1689188420',
    'minisat-hack_1689201742',
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
            GRAPH_TITLE = "Preliminary, {PROGRAM}, {SEARCH_STRATEGY}, k-{K}, Percentage View".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
            IMAGE_NAME = "{PROGRAM}_{SEARCH_STRATEGY}_k-{K}_percentage_view".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
        else:
            GRAPH_TITLE = "Preliminary, {PROGRAM}, {SEARCH_STRATEGY}, k-{K}, fitness View".format(PROGRAM=PROGRAM, SEARCH_STRATEGY = SEARCH_STRATEGY, K=K_TH)
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

        plt.xticks(fontsize="20")
        plt.yticks(fontsize="20")

        plt.savefig('./Preliminary_{FILE_NAME}.png'.format(FILE_NAME=IMAGE_NAME), bbox_inches='tight')

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