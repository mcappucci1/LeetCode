class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        powerSet = []

        def backtrack(i, s):
            if i == len(nums):
                nonlocal powerSet
                powerSet.append(s[:])
                return
            backtrack(i+1, s)
            s.append(nums[i])
            backtrack(i+1, s)
            s.pop()

        backtrack(0, [])
        return powerSet