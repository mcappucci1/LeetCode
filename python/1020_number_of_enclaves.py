class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        queue = deque()

        for i in range(m):
            if grid[i][0] == 1:
                grid[i][0] = -1
                queue.append((i,0))
            if n != 1 and grid[i][n-1] == 1:
                grid[i][n-1] = -1
                queue.append((i,n-1))
        
        for i in range(1, n-1):
            if grid[0][i] == 1:
                grid[0][i] = -1
                queue.append((0,i))
            if m != 1 and grid[m-1][i] == 1:
                queue.append((m-1,i))
                grid[m-1][i] = -1
        
        while queue:
            x, y = queue.popleft()
            for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (0 <= x + i < m) and (0 <= y + j < n) and grid[x+i][y+j] == 1:
                    grid[x+i][y+j] = -1
                    queue.append((x+i, y+j))
        
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
        return total