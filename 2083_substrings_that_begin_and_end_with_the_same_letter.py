class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        total = len(s)
        counts = [0] * 26
        norm = ord('a')

        for i in range(len(s)):
            total += counts[ord(s[i]) - norm]
            counts[ord(s[i]) - norm] += 1
        
        return total