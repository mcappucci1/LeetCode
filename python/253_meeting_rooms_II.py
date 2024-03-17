class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        heap = [intervals[0][1]]
        needed = 1

        for i in range(1, len(intervals)):
            while heap and heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
            needed = max(needed, len(heap))
        
        return needed