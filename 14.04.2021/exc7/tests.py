import unittest

from exc7 import perform_dijkstra_algorithm


class TestDijkstraAlgorithm(unittest.TestCase):
    def test_algorithm(self):
        nodes = ('A', 'B', 'C')
        distances = {
            'A': {'B': 5, 'C': 3},
            'B': {'A': 5, 'C': 1},
            'C': {'A': 3, 'B': 1},
        }
        node = perform_dijkstra_algorithm(nodes, distances)
        total_weigh = sum(node.values())
        self.assertEqual(total_weigh, 7)
