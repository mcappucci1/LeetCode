class Solution:
    def minimumPushes(self, word: str) -> int:

        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        
        counts.sort(reverse=True)
        total = 0

        for i in range(26):
            total += counts[i] * (i // 8 + 1)

        return total