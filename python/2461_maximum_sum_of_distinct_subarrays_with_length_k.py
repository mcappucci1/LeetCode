class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        indexes = dict()
        distinct = -1
        total = 0

        for i in range(k):
            if nums[i] in indexes:
                distinct = max(distinct, indexes[nums[i]])
            indexes[nums[i]] = i
            total += nums[i]
        
        max_sum = total if (distinct == -1) else 0

        for i in range(k, len(nums)):
            if (nums[i] in indexes) and (indexes[nums[i]] > i - k):
                distinct = max(indexes[nums[i]], distinct)
            indexes[nums[i]] = i
            total += nums[i] - nums[i-k]
            if distinct <= i - k:
                max_sum = max(max_sum, total)
        
        return max_sum