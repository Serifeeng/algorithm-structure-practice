## Min Heap

A Min Heap is a complete binary tree where the value of each node is
less than or equal to the values of its children.
The minimum element is always stored at the root.

### Common Use Cases
- Priority queues
- Task scheduling
- Dijkstra’s shortest path algorithm
- Finding the smallest element efficiently

### Time Complexity

| Operation      | Complexity |
|---------------|------------|
| Peek (Min)    | O(1)       |
| Insert        | O(log n)   |
| Remove Min    | O(log n)   |
| Search        | O(n)       |

### Space Complexity
O(n)
