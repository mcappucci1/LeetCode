class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        memo = [[0] * (n+1) for i in range(m+1)]

        for i in range(m+1):
            memo[i][-1] = m - i
        
        for j in range(n+1):
            memo[-1][j] = n - j

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = min(memo[i+1][j+1], memo[i][j+1], memo[i+1][j]) + 1

        return memo[0][0]