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

    def BFS(self, start, target):
        queue = deque()
        visited = set()
        ordered_traversal = []

        queue.append(start)
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(f'Explroing {node}')
            if node == target:
                print(f'Node {node} found ...')
                break
            ordered_traversal.append(node)
            for neighbour in self.adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("BFS traversal order:", ordered_traversal)



graph2 = Graph()
graph2.add_edge('A' , 'B')
graph2.add_edge('A' , 'F')
graph2.add_edge('A' , 'D')
graph2.add_edge('A' , 'E')
graph2.add_edge('B' , 'K')
graph2.add_edge('B' , 'J')
graph2.add_edge('K' , 'N')
graph2.add_edge('K' , 'M')
graph2.add_edge('D' , 'G')
graph2.add_edge('E' , 'C')
graph2.add_edge('E' , 'H')
graph2.add_edge('E' , 'I')
graph2.add_edge('I' , 'L')

print("Adjacency List:")
graph2.print_graph()
graph2.BFS('A' , target = 'G')


