class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:

        total_time = 0
        jobs.sort(reverse=True)
        workers.sort(reverse=True)

        for i in range(len(jobs)):
            total_time = max(total_time, ceil(jobs[i] / workers[i]))

        return total_time