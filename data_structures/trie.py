class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word exists in the trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    trie.insert("app")
    trie.insert("apply")

    print(trie.search("apple"))   # True
    print(trie.search("app"))     # True
    print(trie.search("appl"))    # False

    print(trie.starts_with("app"))  # True
    print(trie.starts_with("bat"))  # False

