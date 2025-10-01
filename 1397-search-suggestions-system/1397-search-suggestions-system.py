class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode with an empty dictionary for children and
        a boolean flag to mark if it's the end of a word.
        """
        self.children = {}  
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        """
        Initializes the Trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.
        Returns True if the word is found, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def _collect_words(self, node: TrieNode, prefix: str, words: list):
        """A recursive helper function to collect all words in the subtree."""
        if len(words)==3:return
        if node.is_end_of_word:
            words.append(prefix)

        for char in sorted(node.children.keys()):
            self._collect_words(node.children[char], prefix + char, words)
            if len(words)>=3:return

    def starts_with(self, prefix: str) -> bool:
        """
        Checks if any word in the Trie starts with the given prefix.
        Returns True if a prefix is found, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        matching_words = []
        self._collect_words(node, prefix, matching_words)
        return matching_words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:trie.insert(product)
        ans = []
        s = ''
        for ch in searchWord:
            s+=ch
            ans.append(trie.starts_with(s))
        return ans