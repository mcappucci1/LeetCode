class Solution:
    def findPeakElement(self, nums: List[int]) -> int:        
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            m = (hi + lo) // 2
            if m < n-1 and nums[m] < nums[m+1]:
                lo = m + 1
            elif m > 0 and nums[m] < nums[m-1]:
                hi = m - 1
            else:
                return m