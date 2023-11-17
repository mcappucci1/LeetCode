class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = -math.inf
        l, r = 0, len(nums)-1
        while l < r:
            max_pair = max(max_pair, nums[l] + nums[r])
            l += 1
            r -= 1
        return max_pair