def dfs(graph, start, visited=None):
    """
    Performs Depth First Search (DFS) on a graph.

    Parameters:
    graph (dict): Graph represented as an adjacency list
    start: Starting node
    visited (set): Keeps track of visited nodes

    Returns:
    list: Order of visited nodes
    """

    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    # Visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

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
    traversal = dfs(graph, start_node)

    print(f"DFS traversal starting from {start_node}: {traversal}")
