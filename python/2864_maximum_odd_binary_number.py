class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        n = len(s)
        s = list(s)
        l, r = -1, n-1

        while r > l:
            if s[r] == '1':
                s[l], s[r] = s[r], s[l]
                while l < r and s[l] == '1':
                    l += 1
            r -= 1

        return ''.join(s)