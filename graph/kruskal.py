class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure with path compression
    and union by rank.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Graph:
    """
    Graph implementation for Kruskal's algorithm.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        """
        Adds an undirected edge to the graph.
        """
        self.edges.append((w, u, v))

    def kruskal(self):
        """
        Runs Kruskal's algorithm to find the Minimum Spanning Tree (MST).

        Returns:
        list: Edges in the MST
        int: Total weight of the MST
        """

        # Sort edges by weight
        self.edges.sort()

        ds = DisjointSet(self.vertices)
        mst = []
        total_weight = 0

        for w, u, v in self.edges:
            if ds.union(u, v):
                mst.append((u, v, w))
                total_weight += w

            if len(mst) == self.vertices - 1:
                break

        return mst, total_weight


if __name__ == "__main__":
    graph = Graph(4)

    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    mst, weight = graph.kruskal()

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")

    print("Total weight:", weight)

