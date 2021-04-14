def print_graph():
    graph = {
        'dom': ['szkola', 'kosciol', 'bar'],
        'szkola': ['szpital', 'dom'],
        'szpital': ['szkola', 'bar', 'kino', 'teatr'],
        'teatr': ['szpital', 'kino'],
        'kino': ['kosciol', 'szpital', 'teatr'],
        'kosciol': ['dom', 'bar', 'kino'],
        'bar': ['kosciol', 'dom', 'szpital'],
    }
    for item in graph:
        for e in graph[item]:
            print(item, '---', e)


if __name__ == '__main__':
    print_graph()
