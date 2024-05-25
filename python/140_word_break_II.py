class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        trav = self.root
        for c in s:
            if c not in trav.children:
                trav.children[c] = TrieNode()
            trav = trav.children[c]
        trav.word = True

    def findAll(self, s, i):
        trav = self.root
        words = []
        for j in range(i, len(s)):
            c = s[j]
            if c not in trav.children:
                break
            trav = trav.children[c]
            if trav.word:
                words.append(s[i:j+1])
        return words


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def recWordBreak(s, trie, i, sentence, answer):
            if i == len(s):
                answer.append(' '.join(sentence))
                return answer
            words = trie.findAll(s, i)
            for word in words:
                sentence.append(word)
                recWordBreak(s, trie, i + len(word), sentence, answer)
                sentence.pop()
            return answer

        trie = Trie()
        for word in wordDict:
            trie.add(word)

        return recWordBreak(s, trie, 0, [], [])