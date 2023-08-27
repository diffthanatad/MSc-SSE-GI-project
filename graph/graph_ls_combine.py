import matplotlib.pyplot as plt
import numpy as np
import csv

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

def main(k_th, view):
    ac = list()
    time_ac = list()
    gi = list()
    time_gi = list()
    ac_gi = list()
    time_ac_gi = list()
    
    for round in range(3):
        if round == 0:
            file_name = ls_ac_gi_logs[k_th - 1]
        elif round == 1:
            file_name = ls_ac_logs[k_th - 1]
        elif round == 2:
            file_name = ls_gi_logs[k_th - 1]

        with open("../results/{}.csv".format(file_name), 'r') as file:
            data = list(csv.reader(file, delimiter=','))
        
        bins = list()
        time = [data[1][2]]
        if view == "Fitness View":
            """ Fitness View """
            bins.append(int(data[1][4]))
        else:
            """ Percentage View """
            bins.append(int(data[1][5]))
        
        N = len(data)
        for i in range(2, N):
            if data[i][4] != 'None':
                if view == "Fitness View":
                    """ Fitness View """
                    bins.append(int(data[i][4]))
                else:
                    """ Percentage View """
                    bins.append(float(data[i][5])) 
                time.append(int(data[i][2]))
        
        if round == 0:
            ac_gi = bins
            time_ac_gi = time
        elif round == 1:
            ac = bins
            time_ac = time
        elif round == 2:
            gi = bins
            time_gi = time
    
    print(time_ac_gi)

    fig = plt.figure()
    fig.set_figwidth(25)
    fig.set_figheight(7)

    plt.plot(time_ac, ac,label = "AC")
    plt.plot(time_gi, gi, label = "GI")
    # plt.plot(time_ac_gi, ac_gi, label = "AC + GI")

    plt.xlabel('Variant')
    plt.title("MiniSAT, Local Search, k-{}, {}".format(k_th, view))
    # plt.grid()

    if view == "Fitness View":
        """ Fitness View """
        plt.ylabel('CPU instructions')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
        plt.savefig('../images/{}_{}_k-{}_fitness_view.png'.format(algorithm, search_space, i_th, view), bbox_inches='tight')
        # plt.show()
    else:
        """ Percentage View """
        plt.ylabel('Percentage')
        # plt.savefig('../images/{}_{}_k-{}_percentage_view.png'.format("LS", k_th, view), bbox_inches='tight')
        plt.show()
    plt.close()
    
for i in range(1):
    # main(i+1, ls_gi_logs[i], "gi", "ls", "Fitness View")
    main(i+1, "Percentage View")

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

# minisat()
# sat4j()