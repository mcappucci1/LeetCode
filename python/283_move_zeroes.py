class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1