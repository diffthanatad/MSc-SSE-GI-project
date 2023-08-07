import matplotlib.pyplot as plt

base_line = 8210340174586
variants = [i for i in range(10)]

ls_ac = [None,7432108132337,8339867303904,None,None,None,7242972744966,8754180974558,None,6752977115812]
ls_gi = [6846201491850,None,7121457871693,None,6728776543409,None,None,None,8672453133876,None]
ls_ac_gi = [None,None,7747779808192,None,None,None,None,7692837460724,None,7399138390255]

ga_ac = [None,None,8255827763805,None,7117904137029,7869973917542,None,7034986726471,7902575626498,None]
ga_gi = [None,7419055909991,None,None,None,7544293823527,None,6887225088091,8877206556775,None]
ga_ac_gi = [None,None,None,None,None,8405936014853,None,None,None,None]

plt.figure()
plt.plot(variants, ls_ac, marker="$c$",  label="First Improvement")
plt.plot(variants, ls_gi, marker="$s$",  label="First Improvement")
plt.plot(variants, ga_ac, marker="$c$", label="Genetic Algorithm")
plt.plot(variants, ga_gi, marker="$s$", label="Genetic Algorithm")

plt.axhline(base_line, linestyle="-", color="m", label="base line")
plt.xticks(variants)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

plt.xlabel('Repetition')
plt.ylabel('CPU instructions')
plt.title("Algorithm Configuration vs. Genetic Improvement")

plt.legend()
plt.grid()
plt.show()