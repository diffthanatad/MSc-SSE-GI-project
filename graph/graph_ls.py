import matplotlib.pyplot as plt
import numpy as np
import csv

def main(i_th, file_name, search_space, algorithm, view):
    fitness = list()
    variant = list()

    try:
        with open("../results-sat4j/{}.csv".format(file_name), 'r') as file:
            data = list(csv.reader(file, delimiter=','))
    except:
        return
    N = len(data)
    for i in range(1, N):
        if data[i][4] != 'None':
            variant.append(int(data[i][0]))
            if view == "Fitness View":
                """ Fitness View """
                fitness.append(int(data[i][4]))
            else:
                """ Percentage View """
                fitness.append(float(data[i][5]))
    
    fig = plt.figure()
    fig.set_figwidth(25)
    fig.set_figheight(7)

    plt.plot(variant, fitness)

    plt.xlabel('Variant')
    plt.title("Sat4j, Local Search, {}, k-{}, {}".format(search_space.upper(), i_th, view))
    plt.grid()

    if view == "Fitness View":
        """ Fitness View """
        plt.ylabel('CPU instructions')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
        plt.savefig('../images/{}_{}_k-{}_fitness_view.png'.format(algorithm, search_space, i_th, view), bbox_inches='tight')
        # plt.show()
    else:
        """ Percentage View """
        plt.ylabel('Percentage')
        plt.savefig('../images/{}_{}_k-{}_percentage_view.png'.format(algorithm, search_space, i_th, view), bbox_inches='tight')
        # plt.show()
    plt.close()

def minisat():
    ls_ac_gi_logs = [
        "ls_ac-gi_1",
        "ls_ac-gi_2",
        "ls_ac-gi_3",
        "ls_ac-gi_4",
        "ls_ac-gi_5",
        "ls_ac-gi_6",
        "ls_ac-gi_7",
        "ls_ac-gi_8",
        "ls_ac-gi_9",
        "ls_ac-gi_10",
    ]
    for i in range(10):
        # main(i+1, ls_ac_gi_logs[i], "ac-gi", "ls", "Fitness View")
        main(i+1, ls_ac_gi_logs[i], "ac-gi", "ls", "Percentage View")

    ls_ac_logs = [
        "ls_ac_1",
        "ls_ac_2",
        "ls_ac_3",
        "ls_ac_4",
        "ls_ac_5",
        "ls_ac_6",
        "ls_ac_7",
        "ls_ac_8",
        "ls_ac_9",
        "ls_ac_10",
    ]
    for i in range(10):
        # main(i+1, ls_ac_logs[i], "ac", "ls", "Fitness View")
        main(i+1, ls_ac_logs[i], "ac", "ls", "Percentage View")

    ls_gi_logs = [
        "ls_gi_1",
        "ls_gi_2",
        "ls_gi_3",
        "ls_gi_4",
        "ls_gi_5",
        "ls_gi_6",
        "ls_gi_7",
        "ls_gi_8",
        "ls_gi_9",
        "ls_gi_10",
    ]
    for i in range(10):
        # main(i+1, ls_gi_logs[i], "gi", "ls", "Fitness View")
        main(i+1, ls_gi_logs[i], "gi", "ls", "Percentage View")

def sat4j():
    ls_ac_gi_logs = [
        "ls_ac-gi_1",
        "ls_ac-gi_2",
        "ls_ac-gi_3",
        "ls_ac-gi_4",
        "ls_ac-gi_5",
        "ls_ac-gi_6",
        "ls_ac-gi_7",
        "ls_ac-gi_8",
        "ls_ac-gi_9",
        "ls_ac-gi_10",
    ]
    for i in range(10):
        # main(i+1, ls_ac_gi_logs[i], "ac-gi", "ls", "Fitness View")
        main(i+1, ls_ac_gi_logs[i], "ac-gi", "ls", "Percentage View")

    ls_ac_logs = [
        "ls_ac_1",
        "ls_ac_2",
        "ls_ac_3",
        "ls_ac_4",
        "ls_ac_5",
        "ls_ac_6",
        "ls_ac_7",
        "ls_ac_8",
        "ls_ac_9",
        "ls_ac_10",
    ]
    for i in range(10):
        # main(i+1, ls_ac_logs[i], "ac", "ls", "Fitness View")
        main(i+1, ls_ac_logs[i], "ac", "ls", "Percentage View")

    ls_gi_logs = [
        "ls_gi_1",
        "ls_gi_2",
        "ls_gi_3",
        "ls_gi_4",
        "ls_gi_5",
        "ls_gi_6",
        "ls_gi_7",
        "ls_gi_8",
        "ls_gi_9",
        "ls_gi_10",
    ]
    for i in range(10):
        # main(i+1, ls_gi_logs[i], "gi", "ls", "Fitness View")
        main(i+1, ls_gi_logs[i], "gi", "ls", "Percentage View")

minisat()
# sat4j()