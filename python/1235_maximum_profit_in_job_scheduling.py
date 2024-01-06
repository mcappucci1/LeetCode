class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)

        jobs = [i for i in range(n)]
        jobs.sort(key=lambda i: startTime[i])

        memo = [0] * n
        memo[-1] = profit[jobs[-1]]

        for i in range(n-2, -1, -1):
            lo, hi = i+1, n-1
            while lo <= hi:
                m = (hi + lo) // 2
                if startTime[jobs[m]] >= endTime[jobs[i]]:
                    hi = m-1
                else:
                    lo = m+1
            memo[i] = max(memo[i+1], profit[jobs[i]] + (memo[lo] if lo < n else 0))
        
        return memo[0]