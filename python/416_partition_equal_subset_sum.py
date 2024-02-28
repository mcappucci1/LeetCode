class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        most = max(nums)

        if total % 2 == 1 or most > total // 2:
            return False

        n = total // 2 + 1
        dp = [True] + [False] * (n-1)

        for num in nums:
            for i in range(n-1, -1, -1):
                dp[i] = dp[i] or (i >= num and dp[i-num])
        
        return dp[-1]