class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count, b_count = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    a_count += 1
                else:
                    b_count += 1
        return a_count > b_count