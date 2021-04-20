def perform_dijkstra_algorithm(nodes, distances):
    unvisited_node = {node: None for node in nodes}
    visited = {}
    start = 'A'
    current_distance = 0
    unvisited_node[start] = current_distance
    while True:
        for neighbour, distance in distances[start].items():
            if neighbour not in unvisited_node: continue
            new_distance = current_distance + distance
            if unvisited_node[neighbour] is None or unvisited_node[neighbour] > new_distance:
                unvisited_node[neighbour] = new_distance
        visited[start] = current_distance
        del unvisited_node[start]
        if not unvisited_node: break
        candidates = [node for node in unvisited_node.items() if node[1]]
        start, current_distance = sorted(candidates, key=lambda x: x[1])[0]
    return visited


if __name__ == '__main__':
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    distances = {
        'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
        'B': {'A': 5, 'D': 1, 'G': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'E': {'G': 2, 'E': 1, 'F': 16},
        'F': {'A': 5, 'E': 2, 'C': 16},
        'G': {'B': 2, 'D': 1, 'C': 2},
    }
    node = perform_dijkstra_algorithm(nodes, distances)
    total_weigh = sum(node.values())
    print(node)
    print(f'Total weight is {total_weigh}')
