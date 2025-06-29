import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random
import sys

"""
This python file contains my self written implementation of using BFS (Breadth-First Search) to traverse Network Notes (Graph) and Visit Every node once.
Network is Graph with Single Source (Start). and BFS goal is to visit every other nodes from Start.
This is not part of book. Rather my Experiment and Another Excellent Way to Visualize BFS.
"""


def build_grid_like_graph(n_rows, n_cols, loop_prob=0.2):
    G = nx.grid_2d_graph(n_rows, n_cols)
    for node in list(G.nodes()):
        if random.random() < loop_prob:
            neighbors = list(G.nodes())
            target = random.choice(neighbors)
            if target != node:
                G.add_edge(node, target)
    mapping = {(i, j): i * n_cols + j for i, j in G.nodes()}
    G = nx.relabel_nodes(G, mapping)
    return G


def build_layered_layout(G, n_cols):
    pos = {}
    for node in G.nodes():
        row = node // n_cols
        col = node % n_cols
        pos[node] = (col, -row)
    return pos


def draw_graph(G, pos, visited, current=None):
    if not plt.get_fignums():
        raise KeyboardInterrupt("❌ Window closed")
    plt.clf()
    node_colors = []
    for node in G.nodes():
        if node == current:
            node_colors.append("red")
        elif node in visited:
            node_colors.append("green")
        else:
            node_colors.append("skyblue")
    nx.draw(G, pos, node_color=node_colors, with_labels=False,
            edge_color='gray', node_size=80)
    plt.title(f"BFS Traversal | Visited: {len(visited)} / {len(G.nodes())}")
    plt.pause(0.01)


def bfs_graph(G, pos, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    fig = plt.figure(1)
    while queue:
        current = queue.popleft()
        draw_graph(G, pos, visited, current)
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    draw_graph(G, pos, visited)
    plt.title("🏁 BFS Complete! Close window to exit.")
    plt.show()


if __name__ == "__main__":
    n_rows = 30
    n_cols = 30
    loop_probability = 0.01  # chance of extra edge (loop)
    G = build_grid_like_graph(n_rows=n_rows, n_cols=n_cols, loop_prob=loop_probability)
    pos = build_layered_layout(G, n_cols=n_cols)
    try:
        bfs_graph(G, pos, start_node=0)
    except KeyboardInterrupt:
        print("✅ Window closed by user.")
        sys.exit(0)
