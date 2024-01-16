class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        norm = ord('a')
        indexes = [0] * 26
        for i in range(26):
            indexes[ord(keyboard[i]) - norm] = i
        
        i = 0
        dist = 0
        for c in word:
            j = indexes[ord(c) - norm]
            dist += abs(i - j)
            i = j

        return dist