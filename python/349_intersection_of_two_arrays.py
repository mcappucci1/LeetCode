class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        seen = [False] * 1001
        for num in nums1:
            seen[num] = True
        
        intersect = []
        
        for num in nums2:
            if seen[num]:
                seen[num] = False
                intersect.append(num)
        
        return intersect