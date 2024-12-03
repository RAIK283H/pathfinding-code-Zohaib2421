import math
import unittest

import pathing
import graph_data, global_game_data
import permutation
import f_w


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

    # def test_get_random_path(self):
    #     path = pathing.get_random_path()
    #     current_graph = graph_data.graph_data[global_game_data.current_graph_index]

    #     self.assertEqual(path[0], 0, "Path does not start at the correct node")
    #     self.assertIn(global_game_data.target_node[global_game_data.current_graph_index], path, "Target is not reached in the graph traversal")
    #     self.assertEqual(path[-1], len(current_graph) - 1, "Path does not end at the correct ending node")

    # def test_get_path(self):
    #     graph = graph_data.graph_data[global_game_data.current_graph_index]
    #     start = 0
    #     end = len(graph) - 1
    #     path = pathing.get_path(graph, start, end)

    #     self.assertEqual(path[0], start, "Path does not start at the correct node")
    #     self.assertEqual(path[-1], end, "Path does not end at the correct ending node")

    # def test_get_neighbours(self):
    #     graph = graph_data.graph_data[global_game_data.current_graph_index]
    #     node = 10
    #     neighbours = pathing.get_neighbours(graph, node)

    #     self.assertTrue(all(neighbour in graph[node][1] for neighbour in neighbours), "Neighbours not correctly identified")
    #     self.assertNotEqual(neighbours, graph[node][1], "Neighbours were not shuffled")

    # def test_get_bfs_path(self):
    #     path = pathing.get_bfs_path()
    #     current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    #     target = global_game_data.target_node[global_game_data.current_graph_index]

    #     self.assertEqual(path[0], 0, "BFS path does not start at the correct node (0)")
    #     self.assertIn(target, path, "BFS path does not reach the target node")
    #     self.assertEqual(path[-1], len(current_graph) - 1, "BFS path does not end at the correct ending node")

    #     self.assertTrue(all(path[i] in current_graph[path[i-1]][1] for i in range(1, len(path))),
    #                     "BFS path contains nodes that are not connected in the graph")

    # def test_get_dfs_path(self):
    #     path = pathing.get_dfs_path()
    #     current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    #     target = global_game_data.target_node[global_game_data.current_graph_index]

    #     self.assertEqual(path[0], 0, "DFS path does not start at the correct node (0)")
    #     self.assertIn(target, path, "DFS path does not reach the target node")
    #     self.assertEqual(path[-1], len(current_graph) - 1, "DFS path does not end at the correct ending node")
    #     self.assertTrue(all(path[i] in current_graph[path[i-1]][1] for i in range(1, len(path))),
    #                     "DFS path contains nodes that are not connected in the graph")

    def test_sjt_permutations(self):
        self.assertEqual(permutation.sjt([1]), [[1]], 'SJT does not give correct permutations with 1 value')
        self.assertEqual(permutation.sjt([1, 2]), [[1, 2], [2, 1]], 'SJT does not give correct permutations with 2 values')
        self.assertEqual(permutation.sjt([1, 2, 3]), [ [1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3] ], 'SJT does not give correct permutations with 3 values')

    def test_hamiltonian_cycles(self):
        graph = [
            [(0, 0), [1, 3]],
            [(1, 0), [0, 2]],
            [(2, 0), [1, 3]],
            [(3, 0), [0, 2]],
        ]
        self.assertNotEqual(permutation.detect_hamiltonian_cycle(graph), -1, 'Does not find cycle graph')
        another = [
            [(0, 0), [1, 2]],
            [(1, 0), [0, 2, 3]],
            [(2, 0), [0, 1, 3, 4]],
            [(3, 0), [1, 2, 4]],
            [(4, 0), [2, 3]]
        ]
        self.assertNotEqual(permutation.detect_hamiltonian_cycle(another), -1, 'Does not find a cycle in another graph')
        self.assertEqual(permutation.detect_hamiltonian_cycle(graph_data.graph_data[0]), -1, 'Finds non-present cycle in graph[0]')
        self.assertEqual(permutation.detect_hamiltonian_cycle(graph_data.graph_data[0]), -1, 'Finds non-present cycle in graph[1]')
    
    def test_dijkstra_on_big_graph(self):
        graph = graph_data.graph_data[2]
        start = 0
        target = 22
        end = len(graph) - 1

        first_part = pathing.dijkstra(start, target, graph)
        first_part.pop()
        second_part = pathing.dijkstra(target, end, graph)
        complete_path = first_part + second_part
        expected_path = [0, 22, 0, 21, 23]

        self.assertEqual(complete_path[0], start, "Dijkstra path does not start at the correct node")
        self.assertEqual(complete_path, expected_path, "Dijkstra path does go to the correct nodes")
        self.assertEqual(complete_path[-1], end, "Dijkstra path does not end at the correct ending node")

    def test_dijkstra_on_small_graph(self):
        graph = graph_data.graph_data[0]
        start = 0
        target = 2
        end = len(graph) - 1

        first_part = pathing.dijkstra(start, target, graph)
        first_part.pop()
        second_part = pathing.dijkstra(target, end, graph)
        complete_path = first_part + second_part
        expected_path = [0, 1, 2]

        self.assertEqual(complete_path[0], start, "Dijkstra path does not start at the correct node")
        self.assertEqual(complete_path, expected_path, "Dijkstra path does go to the correct nodes")
        self.assertEqual(complete_path[-1], end, "Dijkstra path does not end at the correct ending node")
    
    def test_floyd_warshall(self):
        graph = graph_data.graph_data[0]
        start = 0
        end = len(graph) - 1
        path = f_w.floyd_warshall_path(graph)
        dijkstra_path = pathing.dijkstra(start, end, graph)

        self.assertEqual(path[0], start, "Floyd-Warshall path does not start at the correct node")
        self.assertEqual(path[-1], end, "Floyd-Warshall path does not end at the correct ending node")
        self.assertTrue(all(path[i] in graph[path[i-1]][1] for i in range(1, len(path))),
                        "Floyd-Warshall path contains nodes that are not connected in the graph")
        self.assertEqual(path, dijkstra_path, "Floyd-Warshall path is not the same as Dijkstra path")
    
    def test_floyd_warshall_on_big_graph(self):
        graph = graph_data.graph_data[2]
        start = 0
        end = len(graph) - 1
        path = f_w.floyd_warshall_path(graph)
        dijkstra_path = pathing.dijkstra(start, end, graph)

        self.assertEqual(path[0], start, "Floyd-Warshall path does not start at the correct node")
        self.assertEqual(path[-1], end, "Floyd-Warshall path does not end at the correct ending node")
        self.assertTrue(all(path[i] in graph[path[i-1]][1] for i in range(1, len(path))),
                        "Floyd-Warshall path contains nodes that are not connected in the graph")
        self.assertEqual(path, dijkstra_path, "Floyd-Warshall path is not the same as Dijkstra path")
    
    def test_floyd_warshall_on_smaller_graph(self):
        graph = graph_data.graph_data[4]
        start = 0
        end = len(graph) - 1
        path = f_w.floyd_warshall_path(graph)
        dijkstra_path = pathing.dijkstra(start, end, graph)
        self.assertEqual(path[0], start, "Floyd-Warshall path does not start at the correct node")
        self.assertEqual(path[-1], end, "Floyd-Warshall path does not end at the correct ending node")
        self.assertTrue(all(path[i] in graph[path[i-1]][1] for i in range(1, len(path))),
                        "Floyd-Warshall path contains nodes that are not connected in the graph")
        self.assertEqual(path, dijkstra_path, "Floyd-Warshall path is not the same as Dijkstra path")

if __name__ == '__main__':
    unittest.main()
