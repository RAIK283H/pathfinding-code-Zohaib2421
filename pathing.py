from collections import deque
import graph_data
import global_game_data
from random import shuffle

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    path = []
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]

    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(curr_graph) - 1

     # Preconditions
    assert curr_graph, "The current graph is empty or null"
    assert 0 <= target < len(curr_graph), "Target is not in the current graph"

    # Get the path from start to target
    # path[0] is the start node
    # path[-1] is the target node
    path += get_path(curr_graph, start, target)
    # Make sure we don't have target node twice in our path array
    path.pop()
    path += get_path(curr_graph, target, end)

    # Post conditions
    assert_path_is_valid(curr_graph, path, target)

    return path

def get_path(graph, start, end):
    # if they're the same node, then just stay at your current node
    if start == end:
        return [start]
    
    path = []
    stack = [start]
    while stack:
        curr_node = stack.pop()
        path.append(curr_node)
        # if we've reached the end node, we've found the path and don't need to continue
        if curr_node == end:
            return path
        for neighbour in get_neighbours(graph, curr_node):
            stack.append(neighbour)

    return path

def get_neighbours(graph, curr_node):
    neighbours = graph[curr_node][1]
    shuffle(neighbours)
    return neighbours


def assert_path_is_valid(graph, path, target):
    # Post conditions for the traversal
    assert path[0] == 0, "Path does not start at the correct node"
    assert target in path, "Target is not reached in the graph traversal"
    assert path[-1] == len(graph) - 1, "Path does not end at the correct ending node"


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
