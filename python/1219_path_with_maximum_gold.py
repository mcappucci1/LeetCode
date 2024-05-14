class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def backtrack(i, j):
            if (not 0 <= i < len(grid)) or (not 0 <= j < len(grid[0])) or (grid[i][j] <= 0):
                return 0
            grid[i][j] = -grid[i][j]
            best = 0
            for a, b in [(1,0),(-1,0),(0,1),(0,-1)]:
                best = max(best, -grid[i][j] + backtrack(i+a, j+b))
            grid[i][j] = -grid[i][j]
            return best

        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                best = max(best, backtrack(i,j))
        
        return best