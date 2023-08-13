class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [True, False, False]
        for i in range(n):
            two_valid = i > 0 and memo[(i - 1) % 3] and nums[i] == nums[i-1]
            three_valid = i > 1 and memo[(i - 2) % 3] and (
                nums[i] == nums[i-1] == nums[i-2] or 
                nums[i-2] + 2 == nums[i-1] + 1 == nums[i]
            )
            memo[(i + 1) % 3] = two_valid or three_valid
        return memo[n % 3]
