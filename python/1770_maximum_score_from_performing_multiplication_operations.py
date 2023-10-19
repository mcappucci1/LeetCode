class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n = len(nums)
        m = len(multipliers)

        memo = [[0] * (m+1) for j in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(m-i-1, -1, -1):
                m = multipliers[i]
                memo[i][j] = max(
                    m * nums[n-j] + memo[i][j+1],
                    m * nums[i-1] + memo[i+1][j]
                )

        return memo[0][0]