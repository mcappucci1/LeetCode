class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] + [0] * (n - 1)
        for i in range(1, n):
            longest = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    longest = max(longest, memo[j] + 1)
            memo[i] = longest
        return max(memo)