class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trustee = [0] * (n+1)
        truster = [False] * (n+1)

        for a, b in trust:
            trustee[b] += 1
            truster[a] = True
        
        for i in range(1, n+1):
            if trustee[i] == (n-1) and (not truster[i]):
                return i
        
        return -1