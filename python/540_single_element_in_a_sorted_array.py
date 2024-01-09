class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            m = (hi + lo) // 2
            if m == 0 and (n == 1 or nums[m] != nums[m+1]):
                hi = m - 1
            elif (m % 2 == 0 and nums[m] == nums[m-1]) or (m % 2 == 1 and nums[m] != nums[m-1]):
                hi = m - 1
            else:
                lo = m + 1
        return nums[max(0, hi)]