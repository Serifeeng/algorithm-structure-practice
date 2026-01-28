def floyd_warshall(graph):
    """
    Runs the Floyd-Warshall algorithm on a weighted graph.

    Parameters:
    graph (list of list): Adjacency matrix where graph[i][j] is the weight
                          of the edge from i to j, or float('inf') if no edge.

    Returns:
    list of list: Matrix of shortest distances between all pairs of vertices
    """

    n = len(graph)

    # Create a copy of the graph to store shortest distances
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    INF = float("inf")

    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]

    distances = floyd_warshall(graph)

    for row in distances:
        print(row)

