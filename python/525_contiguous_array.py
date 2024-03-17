class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_length = 0
        counts = { 0: -1 }
        count = 0

        for i in range(len(nums)):
            count += nums[i] * 2 - 1
            if count not in counts:
                counts[count] = i
            max_length = max(max_length, i - counts[count])

        return max_length