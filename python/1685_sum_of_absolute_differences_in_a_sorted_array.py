class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left = 0
        right = sum(nums)

        for i in range(n):
            left += nums[i]
            right -= nums[i]
            nums[i] = (nums[i] * (i+1) - left) + (right - nums[i] * (n - i - 1))

        return nums