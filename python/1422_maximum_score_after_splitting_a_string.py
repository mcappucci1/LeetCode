class Solution:
    def maxScore(self, s: str) -> int:
        best = -math.inf
        ones = 0
        for i in range(len(s)-1):
            if s[i] == '1':
                ones += 1
            best = max(best, i+1 - ones * 2)
        if s[-1] == '1':
            ones += 1
        return best + ones 