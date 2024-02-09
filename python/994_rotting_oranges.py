class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        total_fresh = 0
        time = 0
        queue = deque()
        seen = [0] * m

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    total_fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        if total_fresh == 0:
            return 0
        
        while queue and total_fresh:
            time += 1
            l = len(queue)
            for i in range(l):
                r, c = queue.popleft()
                for j, k in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if (0 <= j < m) and (0 <= k < n):
                        mask = 1 << k
                        if grid[j][k] == 1 and (seen[j] & mask) == 0:
                            queue.append((j,k))
                            seen[j] |= mask
                            total_fresh -= 1
    
        return time if total_fresh == 0 else -1