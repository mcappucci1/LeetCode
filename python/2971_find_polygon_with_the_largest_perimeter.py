class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        for i in range(len(nums)-1, 1, -1):
            if nums[i] >= total - nums[i]:
                total -= nums[i]
            else:
                return total
        return -1