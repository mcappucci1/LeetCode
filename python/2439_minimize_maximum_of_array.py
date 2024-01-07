class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        total = 0
        smallest_max = 0

        for i in range(len(nums)):
            total += nums[i]
            smallest_max = max(smallest_max, ceil(total / (i+1)))
        
        return smallest_max