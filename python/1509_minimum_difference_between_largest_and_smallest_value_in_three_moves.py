class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) < 5:
            return 0

        min_heap = []
        max_heap = []

        for num in nums:
            if len(max_heap) < 4 or num > max_heap[0]:
                if len(max_heap) == 4:
                    heapq.heappop(max_heap)
                heapq.heappush(max_heap, num)
            if len(min_heap) < 4 or num < -min_heap[0]:
                if len(min_heap) == 4:
                    heapq.heappop(min_heap)
                heapq.heappush(min_heap, -num)

        min_heap = sorted([-num for num in min_heap], reverse=True)
        max_heap.sort()

        diff = inf        
        for i in range(4):
            diff = min(diff, max_heap[-1-i] - min_heap[-1-(3-i)])

        return diff