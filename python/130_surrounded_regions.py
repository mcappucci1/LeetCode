class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])

        stack = []

        for i in range(n):
            if board[0][i] == 'O':
                stack.append((0,i))
                board[0][i] = None
            if m > 1 and board[-1][i] == 'O':
                stack.append((m-1,i))
                board[m-1][i] = None
        
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i,0))
                board[i][0] = None
            if n > 1 and board[i][-1] == 'O':
                stack.append((i,n-1))
                board[i][n-1] = None
        
        while stack:
            r, c = stack.pop()
            for r2, c2 in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (0 <= r2 < m) and (0 <= c2 < n) and (board[r2][c2] == 'O'):
                    stack.append((r2, c2))
                    board[r2][c2] = None
    
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == None:
                    board[r][c] = 'O'