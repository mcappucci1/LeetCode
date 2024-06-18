class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        m, n = len(worker), len(profit)
        worker.sort(reverse=True)
        jobs = [(profit[i], difficulty[i]) for i in range(n)]
        jobs.sort(reverse=True)

        i, j = 0, 0
        total = 0
        while j < n and i < m:
            while i < m and worker[i] >= jobs[j][1]:
                total += jobs[j][0]
                i += 1
            j += 1

        return total