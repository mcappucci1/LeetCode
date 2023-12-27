class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        heap = []
        jobs = [i for i in range(n)]
        jobs.sort(key=lambda i: capital[i])

        for i in jobs:
            while k > 0 and heap and w < capital[i]:
                profit = heapq.heappop(heap)
                w -= profit
                k -= 1
            if k == 0 or w < capital[i]:
                return w
            heapq.heappush(heap, -profits[i])

        while k > 0 and heap:
            profit = heapq.heappop(heap)
            w -= profit
            k -= 1

        return w