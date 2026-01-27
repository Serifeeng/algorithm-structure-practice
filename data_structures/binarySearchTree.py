class Node:
    """
    Represents a node in a Binary Search Tree.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree implementation.
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Inserts a key into the BST.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        # If key == node.key, do nothing (no duplicates)

    def search(self, key):
        """
        Searches for a key in the BST.

        Returns:
        bool: True if key exists, False otherwise
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """
        Returns the inorder traversal of the BST.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Inorder Traversal:", bst.inorder_traversal())
    print("Search 40:", bst.search(40))
    print("Search 90:", bst.search(90))

