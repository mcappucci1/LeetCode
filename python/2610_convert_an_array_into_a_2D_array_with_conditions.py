class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        counts = [0] * (max(nums)+1)
        for num in nums:
            counts[num] += 1
        
        result = [[] for i in range(max(counts))]

        for i in range(len(counts)):
            for j in range(counts[i]):
                result[j].append(i)
        
        return result