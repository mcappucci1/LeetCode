class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        if (m + n) % 2 != 1:
            return False
        
        stack = [(0, 0, grid[0][0] * 2 - 1)]
        seen = set()
        
        while stack:
            x, y, count = stack.pop()
            if x == m-1 and y == n-1 and count == 0:
                return True
            if x < m-1:
                tmp = count + grid[x+1][y] * 2 - 1
                if (x+1, y, tmp) not in seen:
                    stack.append((x+1, y, tmp))
                    seen.add((x+1, y, tmp))
            if y < n-1:
                tmp = count + grid[x][y+1] * 2 - 1
                if (x, y+1, tmp) not in seen:
                    stack.append((x, y+1, tmp))
                    seen.add((x, y+1, tmp))

        return False