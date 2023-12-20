class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        q = deque([(n-1,0,0)])
        seen = [0] * n
        end_c = 0 if n % 2 == 0 else (n-1)

        while q:
            r, c, d = q.popleft()
            back = ((n - r - 1) % 2) == 1
            for j in range(6):
                c += -1 if back else 1
                if not (0 <= c < n):
                    r -= 1
                    c = 0 if c == -1 else (n-1)
                    back = not back
                r2, c2 = r, c
                if board[r2][c2] != -1:
                    x = board[r2][c2] - 1
                    r2 = (n - 1) - (x // n)
                    c2 = (n - (x % n) - 1) if ((r2 % 2) == (n % 2)) else (x % n)
                if (seen[r2] & (1 << c2)) == 0:
                    if (r2 == 0) and (c2 == end_c):
                        return d + 1
                    q.append((r2, c2, d+1))
                    seen[r2] |= 1 << c2
            
        return -1