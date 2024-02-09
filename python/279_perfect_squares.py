class Solution:
    def numSquares(self, n: int) -> int:

        perfect = []
        for i in range(1, floor(sqrt(n)) + 1):
            perfect.append(pow(i, 2))
                
        memo = [inf] * (n + 1)
        memo[n] = 0

        stack = [(n,0)]
        while stack:
            i, c = stack.pop()
            if c > memo[i]:
                continue
            for j in perfect:
                if j > i:
                    break
                elif memo[i] + 1 < memo[i-j]:
                    memo[i-j] = memo[i]+1
                    stack.append((i-j,memo[i-j]))
        
        return memo[0]