
class Graph:
    """
    Graph implementation for Bellman-Ford algorithm.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        """
        Adds a directed edge to the graph.

        Parameters:
        u (int): Source vertex
        v (int): Destination vertex
        w (int): Weight of the edge
        """
        self.edges.append((u, v, w))

    def bellman_ford(self, source):
        """
        Runs the Bellman-Ford algorithm from a source vertex.

        Parameters:
        source (int): Source vertex

        Returns:
        list or None: List of shortest distances, or None if a negative cycle exists
        """

        # Step 1: Initialize distances
        dist = [float("inf")] * self.vertices
        dist[source] = 0

        # Step 2: Relax edges |V| - 1 times
        for _ in range(self.vertices - 1):
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative weight cycles
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return None

        return dist


if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)
    graph.add_edge(3, 2, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 3, -3)

    source = 0
    distances = graph.bellman_ford(source)

    if
