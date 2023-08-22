import matplotlib.pyplot as plt
import numpy as np
import csv

def main(i_th, file_name, search_space, algorithm, view):
    with open("../results/{}.csv".format(file_name), 'r') as file:
        data = list(csv.reader(file, delimiter=','))

    bins = list()
    if view == "Fitness View":
        """ Fitness View """
        bins.append(np.array(int(data[1][4])))
    else:
        """ Percentage View """
        bins.append(np.array(int(data[1][5])))
    
    N = len(data)
    for i in range(2, N, 10):
        temp = list()
        for j in range(10):
            if i+j >= N:
                break
            if data[i+j][4] != 'None':
                if view == "Fitness View":
                    """ Fitness View """
                    temp.append(int(data[i+j][4]))
                else:
                    """ Percentage View """
                    temp.append(float(data[i+j][5])) 
        bins.append(np.array(temp))

    fig = plt.figure()
    fig.set_figwidth(25)
    fig.set_figheight(7)

    plt.boxplot(bins)

    N_bins = len(bins)
    if i_th == 9:
        ticks = np.linspace(0, N_bins, dtype = int, num = (N_bins // 20))
    else:
        ticks = np.linspace(0, N_bins, dtype = int, num = (N_bins // 10))
    plt.xticks(ticks, ticks)

    plt.xlabel('Generation')
    plt.title("Genetic Algorithm, {}, k-{}, {}".format(search_space.upper(), i_th, view))
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

ga_ac_gi_logs = [
    "ga100_ac-gi_1",
    "ga100_ac-gi_2",
    "ga100_ac-gi_3",
    "ga100_ac-gi_4",
    "ga100_ac-gi_5",
    "ga100_ac-gi_6",
    "ga100_ac-gi_7",
    "ga100_ac-gi_8",
    "ga100_ac-gi_9",
    "ga100_ac-gi_10",
]
for i in range(10):
    # main(i+1, ga_ac_gi_logs[i], "ac-gi", "ga100", "Fitness View")
    main(i+1, ga_ac_gi_logs[i], "ac-gi", "ga100", "Percentage View")

ga_ac_logs = [
    "ga100_ac_1",
    "ga100_ac_2",
    "ga100_ac_3",
    "ga100_ac_4",
    "ga100_ac_5",
    "ga100_ac_6",
    "ga100_ac_7",
    "ga100_ac_8",
    "ga100_ac_9",
    "ga100_ac_10",
]
for i in range(10):
    # main(i+1, ga_ac_logs[i], "ac", "ga100", "Fitness View")
    main(i+1, ga_ac_logs[i], "ac", "ga100", "Percentage View")

ga_gi_logs = [
    "ga100_gi_1",
    "ga100_gi_2",
    "ga100_gi_3",
    "ga100_gi_4",
    "ga100_gi_5",
    "ga100_gi_6",
    "ga100_gi_7",
    "ga100_gi_8",
    "ga100_gi_9",
    "ga100_gi_10",
]
for i in range(10):
    # main(i+1, ga_gi_logs[i], "gi", "ga100", "Fitness View")
    main(i+1, ga_gi_logs[i], "gi", "ga100", "Percentage View")