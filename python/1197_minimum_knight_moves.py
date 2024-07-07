class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        if x == 0 and y == 0:
            return 0
        
        steps = 0
        moves = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
        q = deque([(0,0)])
        seen = set()

        while q:
            l = len(q)
            steps += 1
            for i in range(l):
                r, c = q.popleft()
                for i, j in moves:
                    r2, c2 = r + i, c + j
                    if r2 == y and c2 == x:
                        return steps
                    if (r2, c2) not in seen:
                        seen.add((r2,c2))
                        q.append((r2,c2))