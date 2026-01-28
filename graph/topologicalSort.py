from collections import deque


class Graph:
    """
    Directed graph implementation for Topological Sort.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        """
        Adds a directed edge u -> v.
        """
        self.graph[u].append(v)

    def topological_sort(self):
        """
        Performs topological sorting using Kahn's Algorithm (BFS).

        Returns:
        list: Topological order of vertices
        """

        in_degree = [0] * self.vertices

        # Calculate in-degrees
        for u in range(self.vertices):
            for v in self.graph[u]:
                in_degree[v] += 1

        # Queue for vertices with in-degree 0
        queue = deque()
        for i in range(self.vertices):
            if in_degree[i] == 0:
                queue.append(i)

        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # If topo_order doesn't contain all vertices, there's a cycle
        if len(topo_order) != self.vertices:
            raise ValueError("Graph contains a cycle. Topological sort not possible.")

        return topo_order


if __name__ == "__main__":
    graph = Graph(6)

    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    print("Topological Sort Order:")
    print(graph.topological_sort())

