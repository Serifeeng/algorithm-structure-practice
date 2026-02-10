
class SegmentTree:
    """
    Segment Tree implementation for range sum queries.
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index, value):
        """
        Updates the value at a specific index.
        """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, left, right):
        """
        Returns the sum in the range [left, right].
        """
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # No overlap
        if right < start or end < left:
            return 0

        # Total overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, left, right)
        right_sum = self._query(2 * node + 2, mid + 1, end, left, right)

        return left_sum + right_sum


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(data)

    print("Sum of range [1, 3]:", st.query(1, 3))  # 3 + 5 + 7 = 15

    st.update(1, 10)  # Update index 1 to value 10
    print("Sum of range [1, 3] after update:", st.query(1, 3))  # 10 + 5 + 7 = 22
