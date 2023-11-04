class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefixes = { 0: -1 }
        total = 0
        longest = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in prefixes:
                prefixes[total] = i
            if (total - k) in prefixes:
                longest = max(longest, i - prefixes[total - k])
        
        return longest