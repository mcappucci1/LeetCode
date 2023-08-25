class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        n = len(s1) + 1
        m = len(s2) + 1
        memo = [False for j in range(m)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    memo[j] = True
                elif i == 0:
                    memo[j] = memo[j-1] and s2[j-1] == s3[j+i-1]
                elif j == 0:
                    memo[j] = memo[j] and s1[i-1] == s3[i+j-1]
                else:
                    memo[j] = (
                        (s1[i-1] == s3[i+j-1] and memo[j]) or
                        (s2[j-1] == s3[i+j-1] and memo[j-1])
                    )

        return memo[m-1]