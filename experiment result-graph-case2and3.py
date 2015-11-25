import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data
x= [1, 2 ,3, 4, 5]


out_metric = [[0.453488372,0.910691824,0.356168831,0.523993559,0.307134293],
            [0.727131783,0.990566038,  0.755844156,  0.778985507,
            0.762470024], [0.695736434,  0.995283019,  0.825252525,
            0.811594203,  0.815347722], [0.730725129,  0.995283019,
            0.825252525,  0.678234031,  0.815347722] ]

out_accuate =[[0.395349,0.886792,0.558442,0.543478,0.281475],
[0.55814,0.962264,0.761905,0.717391,0.651079],
[0.488372,0.981132,0.935065,0.789855,0.76259],
[0.558349,0.981132,0.935065,0.640915,0.76259]
]

out_testNum = [[9.906977,13.03774,14.51948,10.4058,12.7554],
[13.02326,13.69811,9.969697,8.492754,8.334532],
[18.03488,14.69811,17.18182,11.3913,21.10522],
[18.45032,14.838,17.66073,12.49613,20.47677]]

out_parent = [[0,0,0,0,0],
[0.325581395,0.037735849,0.238095238,0.086956522,0.190647482],
[0.325581395,0.018867925,0.064935065,0,0.079136691],
[0.325581395,0.018867925,0.064935065,0,0.079136691]]

out_child = [[0.418604651,0.037735849,0.619047619,0.449275362,0.918165468],
[0.11627907,0,0.025974026,0.137681159,0.125899281],
[0.186046512,0,0.069264069,0.210144928,0.158273381],
[0.116069121,0,0.069264069,0.228858025,0.158273381]]

out_ignore = [[0.255813953,0.075471698,0.021645022,0.057971014,0.083633094],
[0.069767442,0,0.077922078,0.137681159,0.190647482],
[0.069767442,0,0.034632035,0.079710145,0.158273381],
[0.069767442,0,0.034632035,0.20993693,0.158273381]]

out_irrelevant = [[0.581395349,0.075471698,2.225108225,0.956521739,2.206834532],
[0.279069767,0,0.294372294,0.123188406,0.032374101],
[0.279069767,0,0.294372294,0.086956522,0],
[0.279069767,0,0.294372294,0.204736983,0]]



#define figure and figure size figsize=(width, height)
fig = plt.figure(figsize=(9, 20))

#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18


axmetric = fig.add_subplot(4,2,6) #gas1
axmetricn = fig.add_subplot(4,2,6, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud
axmetricn1 = fig.add_subplot(4,2,6, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud
axmetricn2 = fig.add_subplot(4,2,6, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud


axaccuate = fig.add_subplot(4,2,1) #out9
axaccuaten = fig.add_subplot(4,2,1, sharex=axaccuate,sharey=axaccuate, frameon=False) #out9
axaccuaten1 = fig.add_subplot(4,2,1, sharex=axaccuate, sharey=axaccuate, frameon=False) #gas1 nomeeritud
axaccuaten2 = fig.add_subplot(4,2,1, sharex=axaccuate, sharey=axaccuate, frameon=False) #gas1 nomeeritud


axtestnum = fig.add_subplot(4,2,7) #out8
axtestnumn = fig.add_subplot(4,2,7, sharex=axtestnum, sharey=axtestnum, frameon=False) #out8
axtestnumn1 = fig.add_subplot(4,2,7, sharex=axtestnum, sharey=axtestnum, frameon=False) #gas1 nomeeritud
axtestnumn2 = fig.add_subplot(4,2,7, sharex=axtestnum, sharey=axtestnum, frameon=False) #gas1 nomeeritud



axparent = fig.add_subplot(4,2,3) #out8
axparentn = fig.add_subplot(4,2,3, sharex=axparent, sharey=axparent, frameon=False) #out8
axparentn1 = fig.add_subplot(4,2,3, sharex=axparent, sharey=axparent, frameon=False) #gas1 nomeeritud
axparentn2 = fig.add_subplot(4,2,3, sharex=axparent, sharey=axparent, frameon=False) #gas1 nomeeritud


axchild = fig.add_subplot(4,2,2) #out8
axchildn = fig.add_subplot(4,2,2, sharex=axchild, sharey=axchild, frameon=False) #out8
axchildn1 = fig.add_subplot(4,2,2, sharex=axchild, sharey=axchild, frameon=False) #gas1 nomeeritud
axchildn2 = fig.add_subplot(4,2,2, sharex=axchild, sharey=axchild, frameon=False) #gas1 nomeeritud

axignore = fig.add_subplot(4,2,4) #out8
axignoren = fig.add_subplot(4,2,4, sharex=axignore, sharey=axignore, frameon=False) #out8
axignoren1 = fig.add_subplot(4,2,4, sharex=axignore, sharey=axignore, frameon=False) #gas1 nomeeritud
axignoren2 = fig.add_subplot(4,2,4, sharex=axignore, sharey=axignore, frameon=False) #gas1 nomeeritud

axirrelevant = fig.add_subplot(4,2,5) #out8
axirrelevantn = fig.add_subplot(4,2,5, sharex=axirrelevant, sharey=axirrelevant, frameon=False) #out8
axirrelevantn1 = fig.add_subplot(4,2,5, sharex=axirrelevant, sharey=axirrelevant, frameon=False) #gas1 nomeeritud
axirrelevantn2 = fig.add_subplot(4,2,5, sharex=axirrelevant, sharey=axirrelevant, frameon=False) #gas1 nomeeritud


#plot data and normalized data 
line_1, = axmetric.plot(x, out_metric[0],  marker="s",  color="k")
line_2, = axmetricn.plot(x, out_metric[1], ls="--", marker="d",   color="k")
line_3, = axmetricn1.plot(x, out_metric[2], ls=":", marker="o", mfc="None",   color="k")
line_4, = axmetricn2.plot(x, out_metric[3], ls="-.", marker="*", mfc="None",   color="k")

axaccuate.plot(x, out_accuate[0],  marker="s", color="k")
axaccuaten.plot(x, out_accuate[1], ls="--", marker="d",   color="k")
axaccuaten1.plot(x, out_accuate[2], ls=":", marker="o", mfc="None",   color="k")
axaccuaten2.plot(x, out_accuate[3], ls="-.", marker="*", mfc="None",   color="k")

axtestnum.plot(x, out_testNum[0],  marker="s", color="k")
axtestnumn.plot(x, out_testNum[1], ls="--",marker="d",  color="k")
axtestnumn1.plot(x, out_testNum[2], ls=":", marker="o", mfc="None",   color="k")
axtestnumn2.plot(x, out_testNum[3], ls="-.", marker="*", mfc="None",   color="k")


axparent.plot(x, out_parent[0],  marker="s", color="k")
axparentn.plot(x, out_parent[1], ls="--",marker="d",  color="k")
axparentn1.plot(x, out_parent[2], ls=":", marker="o", mfc="None",   color="k")
axparentn2.plot(x, out_parent[3], ls="-.", marker="*", mfc="None",   color="k")


axchild.plot(x, out_child[0],  marker="s", color="k")
axchildn.plot(x, out_child[1], ls="--",marker="d", color="k")
axchildn1.plot(x, out_child[2], ls=":", marker="o", mfc="None",   color="k")
axchildn2.plot(x, out_child[3], ls="-.", marker="*", mfc="None",   color="k")


axignore.plot(x, out_ignore[0],  marker="s", color="k")
axignoren.plot(x, out_ignore[1], ls="--",marker="d",color="k")
axignoren1.plot(x, out_ignore[2], ls=":", marker="o", mfc="None",   color="k")
axignoren2.plot(x, out_ignore[3], ls="-.", marker="*", mfc="None",   color="k")


axirrelevant.plot(x, out_irrelevant[0],  marker="s", color="k")
axirrelevantn.plot(x, out_irrelevant[1], ls="--",marker="d", color="k")
axirrelevantn1.plot(x, out_irrelevant[2], ls=":", marker="o", mfc="None",   color="k")
axirrelevantn2.plot(x, out_irrelevant[3], ls="-.", marker="*", mfc="None",   color="k")
#configure legend
fig.legend([line_1, line_2, line_3, line_4], ['regard one', 'distin', 'ILP', 'random'],'upper left',
           ncol=4,prop={'size':10})


#configure axis

#1233
#axmetric.set_ylim(0, 1.05)
#axaccuate.set_ylim(0, 1.05)
#axtestnum.set_ylim(0, 1.05)

#axmetric.set_yticks(np.arange(0.7, 1.05, 0.1))
#axaccuate.set_yticks(np.arange(0.8, 1.05, 0.1))
#axtestnum.set_yticks(np.arange(0.8, 1.05, 0.1))

#hide Y tick labels for some plots(only plots on the left and right have labels and ticklabels
##axaccuate.set_yticklabels([]) 
##axtestnum.set_yticklabels([])

axmetric.set_xlim(1, 5)
axaccuate.set_xlim(1, 5)
axtestnum.set_xlim(1, 5)

#axmetric.set_xticks(np.arange(2, 4, 1))
#axaccuate.set_xticks(np.arange(2, 5, 1))
#axtestnum.set_xticks(np.arange(2, 6, 1))


#axmetric.set_xticklabels(['2','3'])
#axaccuate.set_xticklabels(['2','3','4'])
#axtestnum.set_xticklabels(['2','3','4','5'])



#axmetric.set_xticklabels(['2','3'])
#axaccuate.set_xticklabels(['2','3','4'])
#axtestnum.set_xticklabels(['2','3','4','5'])



#disable labels for some plots
##axmetricn.set_yticklabels([])
##axaccuaten.set_yticklabels([])
##axtestnumn.set_yticklabels([])
##
##ax4n.set_yticklabels([])
##ax5n.set_yticklabels([])
##ax6n.set_yticklabels([])


axmetric.yaxis.tick_left()
axaccuate.yaxis.tick_left()
axtestnum.yaxis.tick_left()


#set Y labels
axaccuate.set_xlabel(r"$(a)\ Result\ of\ the\ number\ of\ accurately\ identified\ MFS$")
axmetric.set_xlabel(r"$(f)\ The\ aggregative\ result\ for\ the\ five\ metrics$")
axtestnum.set_xlabel(r"$(g)\ Needed\ test\ cases$")
axparent.set_xlabel(r"$(c)\ Result\ of\ the\ number\ of\ identified\ super-schemas\ of\ the\ MFS$")
axchild.set_xlabel(r"$(b)\ Result\ of\ the\ number\ of\ identified\ sub-schemas\ of\ the\ MFS$")
axignore.set_xlabel(r"$(d)\ Result\ of\ the\ number\ of\ ignored\ MFS$")
axirrelevant.set_xlabel(r"$(e)\ Result\ of\ the\ number\ of\ identified\ irrelevant\ schemas\ of\ the\ MFS$")


#set X labels
axmetric.set_ylabel(r"$AGGREGATIVE\ VALUE$")
axaccuate.set_ylabel(r"$ACCURATE\ NUMBER$")
axtestnum.set_ylabel(r"$NUMBER\ OF\ TEST\ CASES$")
axparent.set_ylabel(r"$SUPER\ NUMBER$")
axchild.set_ylabel(r"$SUB\ NUMBER$")
axignore.set_ylabel(r"$IGNORE\ NUMBER$")
axirrelevant.set_ylabel(r"$RRELEVANT\ NUMBER$")

#adjust plot spacing
plt.subplots_adjust(left=0.07, bottom=0.11, right=0.97, top=0.94, wspace=0.25, hspace=0.25)

#finally draw the plot
plt.show()
