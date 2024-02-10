class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        count = n

        def expand(l, r, n):
            total = 0
            while l >= 0 and r < n and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
            return total

        for i in range(n-1):
            count += expand(i-1, i+1, n)
            count += expand(i, i+1, n)

        return count