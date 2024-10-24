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
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(curr_graph) - 1

    def dfs(start_node, end_node):
        stack = [(start_node, [start_node])]
        visited = set()

        while stack:
            curr, path = stack.pop()
            if curr not in visited:
                visited.add(curr)
                if curr == end_node:
                    return path
                
                for neighbor in reversed(curr_graph[curr][1]):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        
        return None

    path_to_target = dfs(start, target)
    path_to_target.pop()
    path_to_exit = dfs(target, end)
    complete_path = path_to_target + path_to_exit

    # Postcondition checks
    assert target in complete_path, "Path does not include the target node"
    assert complete_path[-1] == end, "Path does not end at the exit node"
    assert all(complete_path[i] in curr_graph[complete_path[i-1]][1] for i in range(1, len(complete_path))), \
        "There is not a connecting edge for every pair of sequential vertices in the path"

    return complete_path

def get_bfs_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(curr_graph) - 1

    def bfs(start_node, end_node):
        queue = deque([(start_node, [start_node])])
        visited = set()

        while queue:
            curr, path = queue.popleft()
            if curr not in visited:
                visited.add(curr)
                if curr == end_node:
                    return path
                
                for neighbor in curr_graph[curr][1]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return None

    path_to_target = bfs(start, target)
    path_to_target.pop()
    path_to_exit = bfs(target, end)
    complete_path = path_to_target + path_to_exit

    # Postcondition checks
    assert target in complete_path, "Path does not include the target node"
    assert complete_path[-1] == end, "Path does not end at the exit node"
    assert all(complete_path[i] in curr_graph[complete_path[i-1]][1] for i in range(1, len(complete_path))), \
        "There is not a connecting edge for every pair of sequential vertices in the path"

    return complete_path


def get_dijkstra_path():
    return None
