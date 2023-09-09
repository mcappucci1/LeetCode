class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max_sum = nums[0]
        local_max_sum = nums[0]
        for i in range(1, len(nums)):
            local_max_sum = max(local_max_sum + nums[i], nums[i])
            global_max_sum = max(global_max_sum, local_max_sum)
        return global_max_sum