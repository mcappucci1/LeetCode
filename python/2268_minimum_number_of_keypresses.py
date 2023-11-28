class Solution:
    def minimumKeypresses(self, s: str) -> int:

        counts = [0] * 26
        norm = ord('a')

        for c in s:
            counts[ord(c) - norm] += 1
        
        counts.sort(reverse=True)

        total = 0
        for i in range(26):
            total += counts[i] * (i // 9 + 1)
        
        return total