class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        local_max = nums[0]
        local_min = nums[0]
        for num in nums[1:]:
            tmp = local_max
            local_max = max(local_min * num, local_max * num, num)
            local_min = min(local_min * num, tmp * num, num)
            global_max = max(global_max, local_max)
        return global_max