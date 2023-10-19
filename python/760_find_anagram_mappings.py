class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n = len(nums1)
        
        characterMapping = defaultdict(list)
        for i in range(n):
            characterMapping[nums2[i]].append(i)
        
        resultMapping = []
        for i in range(n):
            resultMapping.append(characterMapping[nums1[i]][-1])
            characterMapping[nums1[i]].pop()
            
        return resultMapping