class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        memo = [0] * (n+1)

        for i in range(1, n+1):
            m = 0
            for j in range(i, max(0, i-k), -1):
                m = max(m, arr[j-1])
                memo[i] = max(memo[i], m * (i-j+1) + memo[j-1])
        
        return memo[-1]