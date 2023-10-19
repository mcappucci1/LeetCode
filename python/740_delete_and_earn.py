class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        n = max(nums)
        memo = [0] * (n+1)
        points = defaultdict(int)
        for num in nums:
            points[num] += num
        
        memo[1] = points[1]
        for i in range(2, n+1):
            memo[i] = max(memo[i-1], points[i] + memo[i-2])
        
        return memo[-1]