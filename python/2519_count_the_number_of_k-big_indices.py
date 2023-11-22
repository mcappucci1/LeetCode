class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:

        n = len(nums)
        big = [1] * n
        heap = []
        for i in range(n):
            if len(heap) < k:
                heapq.heappush(heap, -nums[i])
                big[i] = 0
            elif -nums[i] >= heap[0]:
                big[i] = 0
                heapq.heappushpop(heap, -nums[i])

        heap = []
        for i in range(n-1, -1, -1):
            if len(heap) < k:
                heapq.heappush(heap, -nums[i])
                big[i] = 0
            elif -nums[i] >= heap[0]:
                big[i] = 0 
                heapq.heappushpop(heap, -nums[i])
        
        return sum(big)