class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        memo = [defaultdict(int) for i in range(n)]
        total = 0

        for i in range(1, n):
            for j in range(i):
                a = memo[j][nums[i] - nums[j]]
                total += a
                memo[i][nums[i] - nums[j]] += a + 1
        
        return total