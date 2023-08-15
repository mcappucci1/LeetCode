class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        one_present = False
        for i in range(n):
            one_present = one_present or nums[i] == 1
            if nums[i] <= 0: nums[i] = 1
        if not one_present:
            return 1
        for i in range(n):
            x = abs(nums[i])
            if x <= n and nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1