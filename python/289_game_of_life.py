class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                live_count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x == i and y == j:
                            continue
                        if (0 <= x < m) and (0 <= y < n) and (abs(board[x][y]) == 1):
                            live_count += 1
                if board[i][j] == 1 and (not 2 <= live_count <= 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live_count == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1