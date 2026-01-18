import heapq


def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest paths
    from a start node to all other nodes.

    Parameters:
    graph (dict): Weighted graph represented as an adjacency list
                  {node: [(neighbor, weight), ...]}
    start: Starting node

    Returns:
    dict: Shortest distances from start to each node
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest distances from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")
