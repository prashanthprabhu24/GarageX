import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines
import random
import sys

"""
This python file contains my self written implementation of selection sort GUI as Sorting People based on Height from shortest to tallest
This is not part of book. Rather my Experiment.
"""

user_closed_window = False

def handle_close(event):
    global user_closed_window
    print("Window closed.")
    user_closed_window = True
    plt.close('all')


def draw_cartoon_person(ax, x, height, shirt_color='skyblue', label=None):
    base_y = 0
    scale = 0.02
    person_height = height * scale
    head_radius = 0.15
    head_y = base_y + person_height + head_radius + 0.2
    head = patches.Circle((x, head_y), head_radius, color='#ffdbac', ec='black', zorder=5)
    ax.add_patch(head)
    body = patches.Rectangle((x - 0.1, base_y + 0.2), 0.2, person_height, color=shirt_color, ec='black', zorder=4)
    ax.add_patch(body)
    arm_y = base_y + person_height * 0.75
    ax.add_line(mlines.Line2D([x - 0.2, x + 0.2], [arm_y, arm_y], lw=1.5, color='black'))
    ax.add_line(mlines.Line2D([x, x - 0.1], [base_y + 0.2, base_y - 0.4], lw=1.5, color='black'))
    ax.add_line(mlines.Line2D([x, x + 0.1], [base_y + 0.2, base_y - 0.4], lw=1.5, color='black'))
    if label:
        ax.text(x, head_y + 0.3, f"{label} cm", ha='center', fontsize=8, weight='bold')


def draw_people(heights, current=None, speed=0.4):
    if user_closed_window:
        sys.exit(0)
    plt.clf()
    ax = plt.gca()
    ax.axis('off')
    ax.set_xlim(-1, len(heights))
    ax.set_ylim(-1, 5.5)
    colors = ['skyblue'] * len(heights)
    if current:
        if len(current) > 0: colors[current[0]] = 'red'
        if len(current) > 1: colors[current[1]] = 'green'
        if len(current) > 2: colors[current[2]] = 'orange'
    for i, h in enumerate(heights):
        draw_cartoon_person(ax, i, h, shirt_color=colors[i], label=h)
    plt.title("Sorting People by Height (Selection Sort)", fontsize=14)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.pause(speed)


def selection_sort(heights, speed=0.4):
    n = len(heights)
    for i in range(n):
        if user_closed_window:
            sys.exit(0)
        min_idx = i
        for j in range(i + 1, n):
            draw_people(heights, [i, j, min_idx], speed)
            if heights[j] < heights[min_idx]:
                min_idx = j
                draw_people(heights, [i, j, min_idx], speed)
        heights[i], heights[min_idx] = heights[min_idx], heights[i]
        draw_people(heights, [i, min_idx], speed)
    draw_people(heights, speed=speed)
    plt.show()


heights = random.sample(range(1, 201), 10)
fig = plt.figure()
fig.canvas.mpl_connect('close_event', handle_close)
selection_sort(heights, speed=0.3)
