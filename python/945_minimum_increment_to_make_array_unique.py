class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        total_moves = 0
        large = nums[0] + 1

        for i in range(1, len(nums)):
            if nums[i] >= large:
                large = nums[i] + 1
            else:
                total_moves += large - nums[i]
                large += 1

        return total_moves