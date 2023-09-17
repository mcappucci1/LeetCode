class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        total = 0
        min_length = float('inf')
        
        for end in range(len(nums)):
            total += nums[end]
            while total >= target and start <= end:
                min_length = min(min_length, end - start + 1)
                total -= nums[start]
                start += 1
        
        return 0 if min_length == float('inf') else min_length