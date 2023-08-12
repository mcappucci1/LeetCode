class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [[0 for i in range(n)] for j in range(m)]

        memo[0][0] = 1
    
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            memo[i][0] = 1
        
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            memo[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = 0 if obstacleGrid[i][j] == 1 else (memo[i-1][j] + memo[i][j-1])
        
        return memo[m-1][n-1]