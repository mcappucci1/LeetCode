class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        first = [-1] * 26
        last = [-1] * 26
        norm = ord('a')

        for i in range(len(s)):
            x = ord(s[i]) - norm
            if first[x] == -1:
                first[x] = i
            last[x] = i
        
        total = 0

        for i in range(26):
            if first[i] == -1:
                continue
            seen = [False] * 26
            for j in range(first[i] + 1, last[i]):
                seen[ord(s[j]) - norm] = True
            for j in range(26):
                if seen[j]:
                    total += 1

        return total