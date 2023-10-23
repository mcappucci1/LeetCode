class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m = len(nums1)
        n = len(nums2)
        
        seen = set([(0,0)])
        pairs = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        
        while heap and len(pairs) < k:
            total, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in seen:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                seen.add((i+1, j))
            if j+1 < n and (i, j+1) not in seen:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                seen.add((i, j+1))
            
        return pairs