class Solution:
    def numberOfWays(self, s: str) -> int:
        memo = [[0,0,0],[0,0,0]]
        for i in range(len(s)-1, -1, -1):
            x = 1 if s[i] == '1' else 0
            memo[x][2] += memo[(x + 1) % 2][1]
            memo[x][1] += memo[(x + 1) % 2][0]
            memo[x][0] += 1
        return memo[0][2] + memo[1][2]