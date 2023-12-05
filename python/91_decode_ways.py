class Solution:
    def numDecodings(self, s: str) -> int:

        memo = [int(s[-1] != '0'),1]

        for i in range(len(s)-2, -1, -1):
            total = 0
            if s[i] != '0':
                total += memo[0]
                if int(s[i]) * 10 + int(s[i+1]) <= 26:
                    total += memo[1]
            memo[1], memo[0] = memo[0], total
        
        return memo[0]