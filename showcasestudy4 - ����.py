"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def show(ax, x, y_1, y_2):
    n_groups = 5
    

    bar_width = 0.25

    opacity = 0.4

    rects1 = ax.bar(x, y_1, bar_width,
                     color='#000000')

    rects2 = ax.bar(x + bar_width, y_2, bar_width,
                     color='#ffffff')

    height = rects1[0].get_height()
    label = round(y_1,2)
    ax.text(rects1[0].get_x() + rects1[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    height = rects2[0].get_height()
    label = round(y_2,2)
    ax.text(rects2[0].get_x() + rects2[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')
    return rects1, rects2

def show2(ax, x, y_1, y_2, y_3):
    n_groups = 5
    
    bar_width = 0.3

    opacity = 0.4

    rects1 = ax.bar(x, y_1, bar_width,
                     color='#000000')

    rects2 = ax.bar(x + bar_width, y_2, bar_width,
                     color='#ffffff')

    rects3 = ax.bar(x + bar_width + bar_width, y_3, bar_width,
                     alpha=opacity,
                     color='#969696')

    height = rects1[0].get_height()
    label = round(y_1,2)
    ax.text(rects1[0].get_x() + rects1[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    height = rects2[0].get_height()
    label = round(y_2,2)
    ax.text(rects2[0].get_x() + rects2[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    height = rects3[0].get_height()
    label = round(y_3,2)
    ax.text(rects3[0].get_x() + rects3[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    return rects1, rects2, rects3

   
    
if __name__ == "__main__":
    avg = [[0.45753315822384183,0.8255367063492064,0.46871647124822025],
[0.7566666666666667,2.626666666666667,0.7333333333333333],
[8.856666666666667,0.8566666666666667,11.186666666666667],
[0.0,0.39666666666666667,0.0],
[0.33999999999999997,0.1433333333333333,0.13333333333333333],
[1.9666666666666666,0.10666666666666667,2.296666666666667],
[122.27666666666667,104.89,104.89]]
    
    avg1 =[[0.4829482273506245,0.8218989197530864,0.4676969977108275],
[0.6833333333333333,3.0933333333333333,0.7233333333333334],
[16.766666666666666,0.87,17.496666666666666],
[0.0,0.54,0.0],
[0.003333333333333334,0.04,0.0],
[1.0466666666666666,0.19333333333333333,1.8466666666666667],
[225.77333333333334,188.33666666666667,188.33666666666667]
]


    avg3 = [[0.4806092887561384,0.8240671957671958,0.47512431466810184],
[0.69,3.1133333333333333,0.7266666666666667],
[23.35333333333333,0.9466666666666667,22.62],
[0.0,0.5633333333333334,0.0],
[0.0,0.01,0.0],
[0.1733333333333333,0.18000000000000002,1.0266666666666666],
[458.93,358.15,358.15]]


    metric2 =[0.4806092887561384,0.8240671957671958,0.47512431466810184]
    accuate2 = [0.69,3.1133333333333333,0.7266666666666667] 
    parent2 = [23.35333333333333,0.9466666666666667,22.62]
    child2 = [0.0,0.5633333333333334,0.0]
    ignore2 = [0.0,0.01,0.0]
    irrelevant2 = [0.1733333333333333,0.18000000000000002,1.0266666666666666]
    testNum2 = [458.93,358.15]
    
    fig = plt.figure(figsize=(7, 3))

    ax1= fig.add_subplot(1,7,6)
    x = np.array([0])
    rects1, rects2, rects3 = show2(ax1, x, avg[0][0], avg[0][1],avg[0][2])
    ax1.set_xlabel('Aggregative')

    ax2= fig.add_subplot(1,7,1)
    x = np.array([0])
    show2(ax2, x, avg[1][0], avg[1][1],avg[1][2])
    ax2.set_xlabel('Accuate')

    ax3= fig.add_subplot(1,7,2)
    x = np.array([0])
    show2(ax3, x, avg[2][0], avg[2][1], avg[2][2])
    ax3.set_xlabel('Super')

    ax4= fig.add_subplot(1,7,3)
    x = np.array([0])
    show2(ax4, x, avg[3][0], avg[3][1],avg[3][2])
    ax4.set_xlabel('Sub')

    ax5= fig.add_subplot(1,7,4)
    x = np.array([0])
    show2(ax5, x, avg[4][0], avg[4][1],avg[4][2])
    ax5.set_xlabel('Ignore')

    ax6= fig.add_subplot(1,7,5)
    x = np.array([0])
    show2(ax6, x, avg[5][0], avg[5][1], avg[5][2])
    ax6.set_xlabel('Irrelevant')


    ax7= fig.add_subplot(1,7,7)
    x = np.array([0])
    show(ax7, x, avg[6][0], avg[6][1])
    ax7.set_xlabel('TestCase')

    ax1.set_xticklabels([])
    ax2.set_xticklabels([])
    ax3.set_xticklabels([])
    ax4.set_xticklabels([])
    ax5.set_xticklabels([])
    ax6.set_xticklabels([])
    ax7.set_xticklabels([])


    #disable labels for some plots
    ax1.set_yticklabels([])
    ax2.set_yticklabels([])
    ax3.set_yticklabels([])
    ax4.set_yticklabels([])
    ax5.set_yticklabels([])
    ax6.set_yticklabels([])
    ax7.set_yticklabels([])
    ##

    #axmetric.set_ylim(0, 1.05)
    #axaccuate.set_ylim(0, 1.05)
    #axtestnum.set_ylim(0, 1.05)

    high = max(avg[0])
    high = high * 1.28
    ax1.set_ylim(0, high)
    high = max(avg[1])
    high = high * 1.28
    ax2.set_ylim(0, high)
    high = max(avg[2])
    high = high * 1.31
    ax3.set_ylim(0, high)
    high = max(avg[3])
    high = high * 1.28
    ax4.set_ylim(0, high)
    high = max(avg[4])
    high = high * 1.28
    ax5.set_ylim(0, high)
    high = max(avg[5])
    high = high * 1.28
    ax6.set_ylim(0, high)
    high = max(avg[6])
    high = high * 1.38
    ax7.set_ylim(0, high)
    
    
    ax1.set_xlim(-0.08, 1.0)
    ax2.set_xlim(-0.08, 1.0)
    ax3.set_xlim(-0.08, 1.0)
    ax4.set_xlim(-0.08, 1.0)
    ax5.set_xlim(-0.08, 1.0)
    ax6.set_xlim(-0.08, 1.0)
    ax7.set_xlim(-0.04, 0.54)

   # ax1.set_ylabel('number of schemas')
   # plt.title('(a)Result for the 2-way covering array')
   # ax1.set_xticks(x + bar_width, x)
    fig.legend([rects1, rects2, rects3], ['FDA-CIT', 'ILP', 'FDA-CITs'],'upper left',
           ncol=3,prop={'size':10})

    #plt.tight_layout()
    plt.subplots_adjust(left=0.01, bottom=0.26, right=0.97, top=0.88, wspace=0, hspace=0.25)

    plt.show()
