class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n = len(nums)
        memo = [[1] * 1001 for i in range(n)]
        
        best = 1
        for s in range(n-2, -1, -1):
            for e in range(s+1, n):
                diff = nums[s] - nums[e] + 500
                memo[s][diff] = max(memo[s][diff], memo[e][diff] + 1)
                best = max(best, memo[s][diff])

        return best