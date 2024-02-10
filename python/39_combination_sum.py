class Solution:
    def recCombinationSum(self, nums, i, comb, t, res):
        if t == 0:
            res.append(comb[:])
        elif i < len(nums) and nums[i] <= t:
            self.recCombinationSum(nums, i+1, comb, t, res)
            comb.append(nums[i])
            self.recCombinationSum(nums, i, comb, t-nums[i], res)
            comb.pop()
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.recCombinationSum(candidates, 0, [], target, [])