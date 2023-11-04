class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])

        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        seen = set([(start[0], start[1])])
        stack = [(start[0], start[1])]

        while stack:
            x, y = stack.pop()
            if x == destination[0] and y == destination[1]:
                return True
            for a, b in dirs:
                i, j = x, y
                while (0 <= i + a < m) and (0 <= j + b < n) and (maze[i + a][j + b] == 0):
                    i += a
                    j += b
                if (i, j) not in seen:
                    stack.append((i, j))
                    seen.add((i, j))
        
        return False