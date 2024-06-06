import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (станцій)
stations = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
]
G.add_nodes_from(stations)

# Додавання ребер (ліній)
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
    ("D", "F"),
    ("E", "F"),
]
G.add_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    edge_color="gray",
    node_size=2000,
    font_size=15,
)
plt.title("Transport Network Graph")
plt.show()


# Кількість вершин
num_nodes = G.number_of_nodes()
print(f"Number of nodes: {num_nodes}")

# Кількість ребер
num_edges = G.number_of_edges()
print(f"Number of edges: {num_edges}")

# Ступінь вершин
degree = dict(G.degree())
print(f"Degrees of nodes: {degree}")


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


start_node = "A"
end_node = "F"
dfs_paths = list(dfs_path(G, start_node, end_node))
print(f"DFS paths from {start_node} to {end_node}: {dfs_paths}")


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


bfs_paths = list(bfs_path(G, start_node, end_node))
print(f"BFS paths from {start_node} to {end_node}: {bfs_paths}")


# Додавання ваг до ребер
weighted_edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "D", 5),
    ("C", "D", 1),
    ("C", "E", 7),
    ("D", "E", 2),
    ("D", "F", 3),
    ("E", "F", 1),
]
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

# Візуалізація графа з вагами
pos = nx.spring_layout(G_weighted)
nx.draw(
    G_weighted,
    pos,
    with_labels=True,
    node_color="skyblue",
    edge_color="gray",
    node_size=2000,
    font_size=15,
)
edge_labels = nx.get_edge_attributes(G_weighted, "weight")
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)
plt.title("Weighted Transport Network Graph")
plt.show()

# Алгоритм Дейкстри
shortest_path = nx.dijkstra_path(G_weighted, start_node, end_node)
shortest_path_length = nx.dijkstra_path_length(G_weighted, start_node, end_node)
print(
    f"Shortest path from {start_node} to {end_node} using Dijkstra's algorithm: {shortest_path}"
)
print(f"Shortest path length: {shortest_path_length}")
