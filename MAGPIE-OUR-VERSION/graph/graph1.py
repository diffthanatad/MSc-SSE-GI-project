import matplotlib.pyplot as plt

base_line = 8210340174586
variants = [i for i in range(1, 11)]

ls_ac = [None,7432108132337,8339867303904,None,None,None,7242972744966,8754180974558,None,6752977115812]
ls_gi = [6846201491850,None,7121457871693,None,6728776543409,None,None,None,8672453133876,None]
ls_ac_gi = [None,None,7747779808192,None,None,None,None,7692837460724,None,7399138390255]

ga_ac = [None,None,8255827763805,None,7117904137029,7869973917542,None,7034986726471,7902575626498,None]
ga_gi = [None,7419055909991,None,None,None,7544293823527,None,6887225088091,8877206556775,None]
ga_ac_gi = [None,None,None,None,None,8405936014853,None,None,None,None]

f = plt.figure()
f.set_figwidth(25)
f.set_figheight(7)

plt.scatter(variants, ga_ac, marker="*", color="red", s=400)
plt.scatter(variants, ga_gi, marker="o", color="red", s=400)
plt.scatter(variants, ga_ac_gi, marker="D", color="red", s=400)

plt.scatter(variants, ls_ac, marker="*", color="blue", s=400)
plt.scatter(variants, ls_gi, marker="o", color="blue", s=400)
plt.scatter(variants, ls_ac_gi, marker="D", color="blue", s=400)

plt.axhline(base_line, linestyle="-", color="green", label="base line")
plt.xticks(variants, fontsize="20")
plt.yticks(fontsize="20")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
# ax.yaxis.offsetText.set_fontsize(20)
# plt.rc('font', **{'size':'30'})
plt.rcParams.update({'font.size': 22})

plt.plot([], color='blue', label='First Improvement')
plt.plot([], color='red', label='Genetic Algorithm')
# plt.plot([], marker="*", label='AC')
# plt.plot([], marker="o", label='GI')
# plt.plot([], marker="D", label='AC + GI')

plt.xlabel('K-fold', fontsize="20")
plt.ylabel('CPU instructions (x10^12)', fontsize="20")
plt.title("First Improvement vs. Genetic Algorithm", fontsize="20")

plt.legend(fontsize="20")
plt.grid()
# plt.show()
plt.savefig('../images/first_improvement_and_genetic_algorithm_4.png', bbox_inches='tight')