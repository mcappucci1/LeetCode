class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        k = len(nums)
        indexes = [0] * k
        heap = []
        smallest_range = [0, -float('inf')]

        for i in range(k):
            smallest_range[1] = max(smallest_range[1], nums[i][0])
            heapq.heappush(heap, (nums[i][0], i))

        smallest_range[0] = heap[0][0]
        current_range = smallest_range.copy()

        while heap:
            value, list_index = heapq.heappop(heap)
            indexes[list_index] += 1
            if indexes[list_index] == len(nums[list_index]):
                return smallest_range
            heapq.heappush(heap, (nums[list_index][indexes[list_index]], list_index))
            current_range[0] = heap[0][0]
            current_range[1] = max(current_range[1], nums[list_index][indexes[list_index]])
            if (current_range[1] - current_range[0]) < (smallest_range[1] - smallest_range[0]):
                smallest_range = current_range.copy()

        return smallest_range