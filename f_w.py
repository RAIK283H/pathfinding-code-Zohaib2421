example_graph = [
    [(0, 0), [1]],
    [(200, -200), [0, 2]],
    [(200, -400), [1]]
]

def floyd_warshall(graph):
    n = len(graph)
    W = get_weighted_graph(graph)
    P = [[-1 for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][k] + W[k][j] < W[i][j]:
                    W[i][j] = W[i][k] + W[k][j]
                    P[i][j] = k
    return W, P

def get_weighted_graph(graph):
    n = len(graph)
    weighted_graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        weighted_graph[i][i] = 0
        for j in graph[i][1]:
            weighted_graph[i][j] = 1
    return weighted_graph

def floyd_warshall_path(graph):
    W, P = floyd_warshall(graph)
    start, end = 0, len(graph) - 1
    return get_path(P, start, end)

def get_path(P, i, j):
    path = []
    z = P[i][j]
    while z != -1:
        path.append(z)
        z = P[i][z]
    path.insert(0, i)
    path.append(j)
    return path
