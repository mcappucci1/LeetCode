class Solution:
    def countOrders(self, n: int) -> int:

        memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
        memo[0][0] = 1
        MOD = 10 ** 9 + 7
        
        for i in range(n+1):
            for j in range(n+1):
                if i > 0:
                    memo[i][j] += i * memo[i-1][j]
                if j > i:
                    memo[i][j] += (j - i) * memo[i][j-1]
                memo[i][j] %= MOD

        return memo[n][n]