class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
        max_product = 0
        for i in range(2,n):
            if nums[i] > a:
                b, a = a, nums[i]
            elif nums[i] > b:
                b = nums[i]
        return (a-1) * (b-1)