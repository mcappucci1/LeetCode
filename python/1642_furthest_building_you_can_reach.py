class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap = []

        for i in range(len(heights)-1):
            if heights[i] >= heights[i+1]:
                continue
            bricks -= heights[i+1] - heights[i]
            heapq.heappush(heap, heights[i] - heights[i+1])
            while bricks < 0 and ladders > 0:
                bricks += -heapq.heappop(heap)
                ladders -= 1
            if bricks < 0:
                return i

        return len(heights)-1