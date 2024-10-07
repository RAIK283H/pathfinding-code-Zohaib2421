import math
import unittest

from pathing import get_random_path, get_path, get_neighbours
import graph_data, global_game_data


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_get_random_path(self):
        path = get_random_path()
        current_graph = graph_data[global_game_data.current_graph_index]

        self.assertEqual(path[0], 0, "Path does not start at the correct node")
        self.assertIn(global_game_data.target_node[global_game_data.current_graph_index], path, "Target is not reached in the graph traversal")
        self.assertEqual(path[-1], len(current_graph) - 1, "Path does not end at the correct ending node")

    def test_get_path(self):
        graph = graph_data[global_game_data.current_graph_index]
        start = 0
        end = len(graph) - 1
        path = get_path(graph, start, end)

        self.assertEqual(path[0], start, "Path does not start at the correct node")
        self.assertEqual(path[-1], end, "Path does not end at the correct ending node")

    def test_get_neighbours(self):
        graph = graph_data[global_game_data.current_graph_index]
        node = 10
        neighbours = get_neighbours(graph, node)

        self.assertTrue(all(neighbour in graph[node][1] for neighbour in neighbours), "Neighbours not correctly identified")
        self.assertNotEqual(neighbours, graph[node][1], "Neighbours were not shuffled")


if __name__ == '__main__':
    unittest.main()
