class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        memo = [0] * (n+1)

        for i in range(m):
            prev = 0
            for j in range(1, n+1):
                tmp = memo[j]
                memo[j] = max(prev + int(text1[i] == text2[j-1]), memo[j-1], memo[j])
                prev = tmp
        
        return memo[-1]