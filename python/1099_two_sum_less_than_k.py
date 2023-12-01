class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()
        result = -1
        l, r = 0, n-1

        while l < r:
            total = nums[l] + nums[r]
            if total >= k:
                r -= 1
            else:
                result = max(result, total)
                l += 1
        
        return result