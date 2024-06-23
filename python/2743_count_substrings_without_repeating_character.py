class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:

        seen = [-1] * 26
        total = 0
        l = 0

        for r in range(len(s)):
            i = ord(s[r]) - ord('a')
            if seen[i] < l:
                total += r - l + 1
            else:
                l = seen[i] + 1
                total += r - l + 1
            seen[i] = r

        return total