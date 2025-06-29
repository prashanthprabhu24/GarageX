import matplotlib.pyplot as plt
import random
import sys


"""
This python file contains my self written implementation of quick sort GUI as Sorting Sticks/Bars based on Height from shortest to tallest
This is not part of book. Rather my Experiment.
Inspired by "Sorting Out Sorting (1981)".
"""

user_closed_window = False

def handle_close(event):
    global user_closed_window
    print("Window closed by user.")
    user_closed_window = True
    plt.close('all')


def draw_bars(data, pivot_idx=None, swapped_idx=(), sorted_indices=(), delay=0.3):
    if user_closed_window:
        sys.exit(0)
    plt.clf()
    ax = plt.gca()
    ax.set_title("Quick Sort Visualization")
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 10)
    ax.axis('off')
    colors = ['skyblue'] * len(data)
    if pivot_idx is not None:
        colors[pivot_idx] = 'red'
    for i in swapped_idx:
        colors[i] = 'orange'
    for i in sorted_indices:
        colors[i] = 'green'
    bars = plt.bar(range(len(data)), data, color=colors)
    for idx, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 1,
                 str(data[idx]), ha='center', fontsize=7)
    plt.pause(delay)


def quick_sort(data, low, high, delay=0.2, sorted_indices=set()):
    if user_closed_window:
        sys.exit(0)
    if low < high:
        pivot_index = partition(data, low, high, delay, sorted_indices)
        quick_sort(data, low, pivot_index - 1, delay, sorted_indices)
        quick_sort(data, pivot_index + 1, high, delay, sorted_indices)
    if low >= 0 and high >= 0:
        for i in range(low, high + 1):
            sorted_indices.add(i)
        draw_bars(data, None, (), sorted_indices, delay * 0.5)


def partition(arr, low, high, delay, sorted_indices):
    pivot = arr[high]
    pivot_idx = high
    i = low - 1
    for j in range(low, high):
        draw_bars(arr, pivot_idx, (i, j), sorted_indices, delay)
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_bars(arr, pivot_idx, (i, j), sorted_indices, delay)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_bars(arr, pivot_idx, (i + 1, high), sorted_indices, delay)
    return i + 1


data = random.sample(range(1, 201), 50)
fig = plt.figure()
fig.canvas.mpl_connect('close_event', handle_close)
quick_sort(data, 0, len(data) - 1, delay=0.000001)
draw_bars(data, None, (), set(range(len(data))), delay=0.5)
plt.show()
