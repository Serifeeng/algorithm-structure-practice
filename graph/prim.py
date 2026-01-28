import heapq


class Graph:
    """
    Graph implementation for Prim's algorithm using adjacency list.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        """
        Adds an undirected weighted edge to the graph.
        """
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim(self, start=0):
        """
        Runs Prim's algorithm to find the Minimum Spanning Tree (MST).

        Parameters:
        start (int): Starting vertex

        Returns:
        list: Edges in the MST
        int: Total weight of the MST
        """

        visited = [False] * self.vertices
        min_heap = [(0, start, -1)]  # (weight, current, parent)
        mst = []
        total_weight = 0

        while min_heap and len(mst) < self.vertices - 1:
            weight, u, parent = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            total_weight += weight

            if parent != -1:
                mst.append((parent, u, weight))

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))

        return mst, total_weight


if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    mst, weight = graph.prim(start=0)

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")

    print("Total weight:", weight)

