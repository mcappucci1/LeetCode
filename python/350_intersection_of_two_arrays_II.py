class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = [0] * 1001
        counts2 = [0] * 1001

        for num in nums1:
            counts1[num] += 1
        
        for num in nums2:
            counts2[num] += 1
        
        answer = []
        for i in range(1001):
            answer += [i] * min(counts1[i], counts2[i])

        return answer