class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        a1, a2 = 0, 0
        w1, w2 = 0, 0

        while a1 < len(word1) and a2 < len(word2):
            if w1 < len(word1[a1]) and w2 < len(word2[a2]):
                if word1[a1][w1] != word2[a2][w2]:
                    return False
                w1 += 1
                w2 += 1
            else:
                if w1 == len(word1[a1]):
                    w1 = 0
                    a1 += 1
                if w2 == len(word2[a2]):
                    w2 = 0
                    a2 += 1
        
        return a1 == len(word1) and a2 == len(word2)