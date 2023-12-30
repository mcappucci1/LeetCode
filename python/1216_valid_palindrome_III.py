class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        n = len(s)
        memo = [0] * n

        for l in range(n-1,-1,-1):
            prev = 0
            for r in range(l+1, n):
                tmp = memo[r]
                if s[l] == s[r]:
                    memo[r] = prev
                else:
                    memo[r] = min(memo[r], memo[r-1]) + 1
                prev = tmp
        
        return memo[n-1] <= k