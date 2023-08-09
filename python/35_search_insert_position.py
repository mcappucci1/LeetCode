class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] < target:
                lo = m + 1
            elif nums[m] > target:
                hi = m - 1
            else:
                return m
        return lo