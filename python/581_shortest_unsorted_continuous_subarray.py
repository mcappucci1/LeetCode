class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)

        min_out = math.inf
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                min_out = min(min_out, nums[i])

        max_out = -math.inf
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                max_out = max(max_out, nums[i])
        
        l = 0
        while l < n and nums[l] <= min_out:
            l += 1

        r = n-1
        while r > -1 and nums[r] >= max_out:
            r -= 1
        
        return max(0, r - l + 1)