class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        n = len(prob)
        memo = [[0] * (n+1) for i in range(target + 1)]
        memo[0][0] = 1

        for i in range(1, n+1):
            memo[0][i] = memo[0][i-1] * (1-prob[i-1])

        for t in range(1, target+1):
            for c in range(t, n+1):
                memo[t][c] = memo[t-1][c-1] * prob[c-1] + memo[t][c-1] * (1 - prob[c-1])
        
        return memo[target][n]