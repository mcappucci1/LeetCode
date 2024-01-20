class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        def recSolve(surplus, empty):
            if len(empty) == 0:
                return 0
            best = inf
            i, j = empty.pop()
            for r, c in surplus:
                if grid[r][c] > 1:
                    grid[r][c] -= 1
                    best = min(best, abs(r - i) + abs(c - j) + recSolve(surplus, empty))
                    grid[r][c] += 1
            empty.append((i,j))
            return best

        empty = []
        surplus = []
        for r in range(3):
            for c in range(3):
                if grid[r][c] == 0:
                    empty.append((r,c))
                elif grid[r][c] > 1:
                    surplus.append((r,c))

        return recSolve(surplus, empty)