class Solution:
    def minOperations(self, s: str) -> int:

        x, i = True, 0

        for c in s:
            if (c == '1') != x:
                i += 1
            x = not x
        
        return min(i, len(s) - i)