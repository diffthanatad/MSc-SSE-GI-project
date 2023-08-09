import matplotlib.pyplot as plt
import numpy as np
import csv

ga_ac_gi_logs = [
    "ga_ac-gi_1",
    "ga_ac-gi_2",
    "ga_ac-gi_3",
    "ga_ac-gi_4",
    "ga_ac-gi_5",
    "ga_ac-gi_6",
    "ga_ac-gi_7",
    "ga_ac-gi_8",
    "ga_ac-gi_9",
    "ga_ac-gi_10",
]
ga_ac_logs = [
    "ga_ac_1",
    "ga_ac_2",
    "ga_ac_3",
    "ga_ac_4",
    "ga_ac_5",
    "ga_ac_6",
    "ga_ac_7",
    "ga_ac_8",
    "ga_ac_9",
    "ga_ac_10",
]
ga_gi_logs = [
    "ga_gi_1",
    "ga_gi_2",
    "ga_gi_3",
    "ga_gi_4",
    "ga_gi_5",
    "ga_gi_6",
    "ga_gi_7",
    "ga_gi_8",
    "ga_gi_9",
    "ga_gi_10",
]

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

def main(k_th, view):
    ac = list()
    gi = list()
    ac_gi = list()
    
    for round in range(3):
        if round == 0:
            file_name = ga_ac_gi_logs[k_th]
        elif round == 1:
            file_name = ga_ac_logs[k_th]
        elif round == 2:
            file_name = ga_gi_logs[k_th]

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
        
        if round == 0:
            ac_gi = bins
        elif round == 1:
            ac = bins
        elif round == 2:
            gi = bins

    fig = plt.figure()
    fig.set_figwidth(25)
    fig.set_figheight(7)

    print(len(ac), len(gi), len(ac_gi))

    ac_plot = plt.boxplot(ac, positions=np.array(range(len(ac)))*2.0-0.4, widths=0.1)
    gi_plot = plt.boxplot(gi, positions=np.array(range(len(gi)))*2.0+0.4, widths=0.1)
    # ac_gi_plot = plt.boxplot(ac_gi, positions=np.array(range(len(ac_gi)))*2.0+0.4, widths=0.1)
    set_box_color(ac_plot, '#D7191C')
    set_box_color(gi_plot, '#2C7BB6')
    # set_box_color(ac_gi_plot, '#2ca25f')

    # draw temporary red and blue lines and use them to create a legend
    plt.plot([], c='#D7191C', label='ac')
    plt.plot([], c='#2C7BB6', label='gi')
    # plt.plot([], c='#2ca25f', label='ac_gi')
    plt.legend()

    # N_bins = max([len(ac), len(gi), len(ac_gi)])
    # ticks = np.linspace(0, N_bins, dtype = int, num = (N_bins // 5))
    # plt.xticks(ticks, ticks)

    plt.xlabel('Generation')
    plt.title("Genetic Algorithm, k-{}, {}".format(k_th, view))
    plt.grid()

    if view == "Fitness View":
        """ Fitness View """
        plt.ylabel('CPU instructions')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
        plt.savefig('../images/ga_k-{}_fitness_view.png'.format(k_th), bbox_inches='tight')
        # plt.show()
    else:
        """ Percentage View """
        plt.ylabel('Percentage')
        plt.savefig('../images/ga_k-{}_percentage_view.png'.format(k_th), bbox_inches='tight')
        # plt.show()

for i in range(1):
    main(i, "Fitness View")
    # main(i, "Percentage View")