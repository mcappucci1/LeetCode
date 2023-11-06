class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        furthest_jump = 0
        i = 0

        while i <= furthest_jump and furthest_jump < n-1:
            furthest_jump = max(furthest_jump, i + nums[i])
            i += 1

        return furthest_jump >= n-1