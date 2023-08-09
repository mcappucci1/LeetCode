class TrieNode:

    def __init__(self):
        self.children = dict()
        self.word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        trav = self.root
        for c in word:
            if c not in trav.children:
                trav.children[c] = TrieNode()
            trav = trav.children[c]
        trav.word = True

    def traverse(self, target: str) -> TrieNode:
        trav = self.root
        for c in target:
            if c not in trav.children:
                return None
            trav = trav.children[c]
        return trav

    def search(self, word: str) -> bool:
        result = self.traverse(word)
        return bool(result and result.word)

    def startsWith(self, prefix: str) -> bool:
        result = self.traverse(prefix)
        return bool(result)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)