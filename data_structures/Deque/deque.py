from collections import deque

class Deque:
    """
    Deque (Double-Ended Queue) implementation using collections.deque.
    Allows insertion and removal from both ends in O(1) time.
    """

    def __init__(self):
        self.items = deque()

    def add_front(self, item):
        """Adds an item to the front of the deque."""
        self.items.appendleft(item)

    def add_rear(self, item):
        """Adds an item to the rear of the deque."""
        self.items.append(item)

    def remove_front(self):
        """Removes and returns the front item of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.popleft()

    def remove_rear(self):
        """Removes and returns the rear item of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def is_empty(self):
        """Checks if the deque is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the deque."""
        return len(self.items)

    def __repr__(self):
        return f"Deque({list(self.items)})"


if __name__ == "__main__":
    dq = Deque()

    dq.add_rear(10)
    dq.add_rear(20)
    dq.add_front(5)

    print(dq)                # Deque([5, 10, 20])
    print(dq.remove_front()) # 5
    print(dq.remove_rear())  # 20
    print(dq)                # Deque([10])

