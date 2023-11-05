class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total = [1000] * 26
        norm = ord('a')
        for word in words:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - norm] += 1
            for i in range(26):
                total[i] = min(total[i], counts[i])
        result = []
        for i in range(26):
            if total[i] > 0:
                result += [chr(norm + i)] * total[i]
        return result