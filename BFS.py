from collections import deque

def BFS(graph , start):
    queue = deque()
    visited = set()
    ordered_traversal = []

    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(f'Exploring {node}...')
        ordered_traversal.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print(f'visited in BFS : ' , ordered_traversal)


graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

start_node = 'A'
print(f"BFS traversal starting from node '{start_node}':")
BFS(graph, start_node)