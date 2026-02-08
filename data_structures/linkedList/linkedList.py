class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly Linked List implementation.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Adds a node with the given data to the end of the list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        """
        Adds a node with the given data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Deletes the first node with the given key.
        """
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def search(self, key):
        """
        Searches for a value in the list.

        Returns:
        bool: True if found, False otherwise
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def to_list(self):
        """
        Converts the linked list to a Python list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __repr__(self):
        return " -> ".join(map(str, self.to_list())) + " -> None"


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)

    print(ll)              # 5 -> 10 -> 20 -> 30 -> None
    print(ll.search(20))   # True
    print(ll.search(100))  # False

    ll.delete(20)
    print(ll)              # 5 -> 10 -> 30 -> None

