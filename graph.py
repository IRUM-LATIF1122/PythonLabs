from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} --> {self.adj_list[node]}")

    def BFS(self, start):
        queue = deque()
        visited = set()
        ordered_traversal = []

        queue.append(start)
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(f'Exploring {node}...')
            ordered_traversal.append(node)
            for neighbour in self.adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("BFS traversal order:", ordered_traversal)

# Create graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Adjacency List:")
graph.print_graph()

print("\nBFS Traversal:")
graph.BFS(2)


