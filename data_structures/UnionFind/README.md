## Union-Find (Disjoint Set)

Union-Find is a data structure that keeps track of a set of elements
partitioned into disjoint (non-overlapping) subsets.

### Common Use Cases
- Detecting cycles in graphs
- Kruskal’s Minimum Spanning Tree algorithm
- Network connectivity problems
- Dynamic connectivity queries

### Time Complexity

| Operation | Complexity |
|----------|------------|
| Find     | O(α(n))    |
| Union    | O(α(n))    |

*α(n) is the inverse Ackermann function and grows very slowly.*

### Space Complexity
O(n)
