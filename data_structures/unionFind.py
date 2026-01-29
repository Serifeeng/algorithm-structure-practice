class UnionFind:
    def __init__(self, size: int):
        """
        Initializes the Union-Find data structure.
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        """
        Finds the representative (root) of the set that x belongs to.
        Uses path compression for optimization.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Unites the sets that x and y belong to.
        Returns True if union is successful, False if they are already connected.
        """
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


if __name__ == "__main__":
    uf = UnionFind(5)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print(uf.find(0) == uf.find(2))  # True
    print(uf.find(0) == uf.find(3))  # False

