from collections import deque


def bfs(graph, start):
    """
    Performs Breadth First Search (BFS) on a graph.

    Parameters:
    graph (dict): Graph represented as an adjacency list
    start: Starting node

    Returns:
    list: Order of visited nodes
    """

    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        # Visit all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    traversal = bfs(graph, start_node)

    print(f"BFS traversal starting from {start_node}: {traversal}")
