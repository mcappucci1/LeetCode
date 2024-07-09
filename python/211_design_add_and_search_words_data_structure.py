class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        trav = self.root
        for c in word:
            if c not in trav.children:
                trav.children[c] = TrieNode()
            trav = trav.children[c]
        trav.word = True

    def search(self, word: str) -> bool:
        stack = [(0, self.root)]
        while stack:
            i, node = stack.pop()
            if i == len(word):
                if node.word:
                    return True
                continue
            if word[i] == '.':
                for child in node.children.values():
                    stack.append((i+1, child))
            elif word[i] in node.children:
                stack.append((i+1, node.children[word[i]]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)