class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        last_row = 0
        for row in bank:
            curr_row = 0
            for cell in row:
                if cell == '1':
                    curr_row += 1
            if curr_row > 0:
                total += last_row * curr_row
                last_row = curr_row
        return total