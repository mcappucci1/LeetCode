class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row, col, box = 0, 0, 0
            for j in range(9):
                if board[i][j] != '.':
                    val = row ^ (1 << (int(board[i][j]) - 1))
                    if val & row:
                        return False
                    row = val
                if board[j][i] != '.':
                    val = col ^ (1 << (int(board[j][i]) - 1))
                    if val & col:
                        return False
                    col = val
                cell = board[(i // 3) * 3 + (j // 3)][(i % 3) * 3 + (j % 3)]
                if cell != '.':
                    val = box ^ (1 << (int(cell) - 1))
                    if val & box:
                        return False
                    box = val
        
        return True