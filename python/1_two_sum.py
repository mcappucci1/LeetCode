class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [i, m[target - nums[i]]]
            m[nums[i]] = i