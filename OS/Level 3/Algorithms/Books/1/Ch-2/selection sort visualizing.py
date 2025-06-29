import matplotlib.pyplot as plt
import random
import sys


user_closed_window = False

"""
This python file contains my self written implementation of selection sort GUI as Sorting Sticks/Bars based on Height from shortest to tallest
This is not part of book. Rather my Experiment.
Inspired by "Sorting Out Sorting (1981)".
"""


def handle_close(event):
    global user_closed_window
    print("Window closed by user.")
    user_closed_window = True
    plt.close('all')


def draw_data(data, current=None):
    if user_closed_window:
        sys.exit(0)
    plt.clf()
    plt.xticks([])
    plt.yticks([])
    colors = ['skyblue'] * len(data)
    if current:
        if len(current) > 0:
            colors[current[0]] = 'red'
        if len(current) > 1:
            colors[current[1]] = 'green'
        if len(current) > 2:
            colors[current[2]] = 'orange'


    bars = plt.bar(range(len(data)), data, color=colors)
    for idx, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                 str(data[idx]), ha='center', fontsize=8)
    plt.title("Selection Sort Visualization", fontsize=14, weight='bold', pad=10)
    plt.ylim(0, max(data) + 10)
    plt.tight_layout()
    plt.pause(0.000001)


def selection_sort(data):
    n = len(data)
    for i in range(n):
        if user_closed_window:
            sys.exit(0)
        min_idx = i
        for j in range(i + 1, n):
            draw_data(data, [i, j, min_idx])
            if data[j] < data[min_idx]:
                min_idx = j
                draw_data(data, [i, j, min_idx])
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, [i, min_idx])
    draw_data(data)
    plt.show()


data = random.sample(range(1, 101), 30)
fig = plt.figure()
fig.canvas.mpl_connect('close_event', handle_close)
selection_sort(data)
