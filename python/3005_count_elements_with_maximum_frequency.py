class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = [0] * 101
        for num in nums:
            counts[num] += 1
        m = max(counts)
        total = 0
        for c in counts:
            if c == m:
                total += c
        return total