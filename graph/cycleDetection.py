
def has_cycle(graph):
    """
    Detects if a directed graph contains a cycle.

    Parameters:
    graph (dict): Adjacency list representation of the graph

    Returns:
    bool: True if there is a cycle, False otherwise
    """

    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


if __name__ == "__main__":
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["B"]  # cycle here
    }

    if has_cycle(graph):
        print("Graph contains a cycle")
    else:
        print("Graph does not contain a cycle")
