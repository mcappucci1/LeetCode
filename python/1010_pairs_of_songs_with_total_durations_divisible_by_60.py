class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:        
        counts = [0] * 60
        for time in times:
            counts[time % 60] += 1
        total = counts[0] * (counts[0] - 1) // 2 + counts[30] * (counts[30] - 1) // 2
        for i in range(1, 30):
            total += counts[i] * counts[60 - i]
        return total