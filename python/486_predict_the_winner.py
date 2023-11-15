class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        
        memo = [0] * (n+1)

        for l in range(n-1, -1, -1):
            for r in range(l, n+1):
                if l <= r-1:
                    memo[r] = max(nums[l] - memo[r], nums[r-1] - memo[r-1])

        return memo[-1] >= 0