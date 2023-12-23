class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x, y = 0, 0
        seen = set([(0,0)])
        moves = { 'N': (1,0), 'S': (-1,0), 'E': (0,1), 'W': (0,-1) }

        for c in path:
            a, b = moves[c]
            x += a
            y += b
            if (x, y) in seen:
                return True
            seen.add((x,y))
        
        return False