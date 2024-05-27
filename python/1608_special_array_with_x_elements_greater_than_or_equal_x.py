class Solution:
    def specialArray(self, nums: List[int]) -> int:

        large = max(nums)
        counts = [0] * (large + 1)
        total = 0

        for num in nums:
            counts[num] += 1

        for i in range(large, -1, -1):
            total += counts[i]
            if i == total:
                return i
                
        return -1