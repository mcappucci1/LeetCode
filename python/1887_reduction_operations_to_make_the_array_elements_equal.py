class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        total = 0
        for i in range(n-2, -1, -1):
            if nums[i] != nums[i+1]:
                total += n - (i+1)
        return total