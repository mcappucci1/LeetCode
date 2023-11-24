class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)

        queue = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    grid[i][j] = -1
        
        while queue:
            r, c, d = queue.popleft()
            for a, b in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = r + a, c + b
                if (0 <= x < n) and (0 <= y < n) and grid[x][y] == 0:
                    grid[x][y] = d + 1
                    queue.append((x, y, d + 1))
        
        seen = set([(0,0)])
        heap = [(-grid[0][0],0,0)]
        while heap:
            safe, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return max(-safe, 0)
            for a, b in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = r + a, c + b
                if (0 <= x < n) and (0 <= y < n) and (x,y) not in seen:
                    heapq.heappush(heap, (max(safe, -grid[x][y]), x, y))
                    seen.add((x,y))
        