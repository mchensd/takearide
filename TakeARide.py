import matplotlib.pyplot as plt
import numpy as np

def plotter(xAxis, yAxis, axs):
    """
    connects points
    """
    axs[1].plot(xAxis, yAxis, 'bo', xAxis, yAxis, 'b-')
    axs[1].axis([0, 20, 0, 70])
    axs[1].fill_between(xAxis, yAxis, color='#66ccff')



fig, axs = plt.subplots(2, 1)
columns = ['Time (mins)', 'Velocity (mph)']
axs[0].axis('tight')
axs[0].axis('off')

cell_data = [[0,21],
             [2,41],
             [4,25],
             [6,61],
             [8,59],
             [10,13],
             [12,30],
             [14,9],
             [16,26],
             [18,9],
             [20,5]]
             
             
the_table = axs[0].table(colLabels=columns,
                         cellText=cell_data,
                         loc='center',
                         colWidths = [0.2, 0.2])
the_table.set_fontsize(24)
the_table.scale(1.25, 1.25)
plotter([i for i in range(0,21,2)], [21,41,25,61,59,13,30,9,26,9,5], axs)

plt.ylabel("Velocity (mph)", fontsize=18)
plt.xlabel("Time (mins)", fontsize=18)
plt.xticks([i for i in range(2,21,2)])
plt.title("Velocity over time", fontsize=20)

for tick in axs[1].xaxis.get_major_ticks():
    tick.label.set_fontsize(14)

for tick in axs[1].yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
plt.show()
