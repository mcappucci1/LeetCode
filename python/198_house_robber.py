class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back, one_back = 0, 0
        for i in range(len(nums)):
            tmp = one_back
            one_back = max(two_back + nums[i], one_back)
            two_back = tmp
        return one_back