class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def recExists(r, c, l, seen):
            if l == len(word):
                return True
            seen.add((r,c))
            for i, j in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
                if (0 <= i < m) and (0 <= j < n) and ((i,j) not in seen) and board[i][j] == word[l]:
                    if recExists(i, j, l+1, seen):
                        return True
            seen.remove((r,c))
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and recExists(r, c, 1, set([(r,c)])):
                    return True
        
        return False