import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random
import sys


"""
This python file contains my self written implementation of using BFS (Breadth-First Search) to traverse Maze (Graph Like Geometry) and fine Start to End Path.
Maze Can be considered as Graph with Single Source (Start) and Single Destination (End). and BFS goal is to solve the maze by finding correct path from Start to End.
This is not part of book. Rather my Experiment and Excellent Way to Visualize BFS.
"""


def generate_maze(width, height, loop_factor=0.2):
    maze = np.ones((height, width), dtype=np.uint8)
    def neighbors(x, y):
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height:
                yield nx, ny
    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    maze[start_y, start_x] = 0
    walls = [(start_x, start_y)]
    while walls:
        x, y = walls.pop(random.randint(0, len(walls) - 1))
        nbs = list(neighbors(x, y))
        random.shuffle(nbs)
        for nx, ny in nbs:
            wall_x = (x + nx) // 2
            wall_y = (y + ny) // 2
            if maze[ny, nx] == 1 and maze[wall_y, wall_x] == 1:
                maze[ny, nx] = 0
                maze[wall_y, wall_x] = 0
                walls.append((nx, ny))
    for _ in range(int(loop_factor * width * height)):
        x = random.randrange(1, width - 1, 2)
        y = random.randrange(1, height - 1, 2)
        dx, dy = random.choice([(0, 1), (1, 0)])
        wx = x + dx
        wy = y + dy
        if 0 < wx < width and 0 < wy < height:
            if maze[y, x] == 0 and maze[wy, wx] == 0:
                maze[(y + wy) // 2, (x + wx) // 2] = 0
    return maze


def draw_bfs(fig, maze, visited, path=None, delay=0.00001):
    if not plt.get_fignums():
        raise KeyboardInterrupt("❌ Window closed")
    img = np.stack([(1 - maze) * 255] * 3, axis=2)
    for y, x in visited:
        img[y, x] = [173, 100, 230]  # PURPLE (visited)
    if path:
        for y, x in path:
            img[y, x] = [10, 255, 10]  # green (path)
    sy, sx = start
    ey, ex = end
    img[sy, sx-1] = [0, 255, 0]
    img[ey, ex+1] = [255, 0, 0]
    plt.imshow(img, interpolation='nearest', aspect='equal')
    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.text(sx - 8, sy + 0.2, 'START ➝', fontsize=10, color='Green', weight='bold')
    plt.text(ex + 2.5, ey + 0.2, '⬅ END', fontsize=10, color='red', weight='bold')
    if plt.waitforbuttonpress(timeout=delay):
        raise KeyboardInterrupt("❌ Window closed or key pressed")
    plt.clf()


def bfs_on_maze(fig, maze, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}
    visited_order = []
    while queue:
        current = queue.popleft()
        visited_order.append(current)
        if current == end:
            break
        y, x = current
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < maze.shape[0] and 0 <= nx < maze.shape[1]:
                if maze[ny, nx] == 0 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
                    queue.append((ny, nx))
        draw_bfs(fig, maze, visited_order)
    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            break
    path.append(start)
    path.reverse()
    img = np.stack([(1 - maze) * 255] * 3, axis=2)
    for y, x in visited_order:
        img[y, x] = [173, 216, 230]
    for y, x in path:
        img[y, x] = [10, 255, 10]
    sy, sx = start
    ey, ex = end
    img[sy, sx - 1] = [0, 255, 0]
    img[ey, ex + 1] = [0, 255, 0]
    plt.imshow(img, interpolation='nearest', aspect='equal')
    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.title("Path Found! You can now close the window.")
    plt.text(sx - 8, sy + 0.2, 'START ➝', fontsize=10, color='green', weight='bold')
    plt.text(ex + 2.5, ey + 0.2, '⬅ END', fontsize=10, color='red', weight='bold')
    plt.show()


width, height = 51, 51
maze = generate_maze(width, height, loop_factor=0.2)
start = (1, 1)
end = (height - 2, width - 2)
maze[start[0], start[1]] = 0
maze[start[0] + 1, start[1]] = 0
maze[end[0], end[1]] = 0
maze[end[0] - 1, end[1]] = 0
fig = plt.figure(1)
try:
    bfs_on_maze(fig, maze, start, end)
except KeyboardInterrupt as e:
    print(str(e))
    sys.exit(0)
