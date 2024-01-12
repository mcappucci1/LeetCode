class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        result = []
        tallest = -inf

        for i in range(len(heights)-1, -1, -1):
            if heights[i] > tallest:
                result.append(i)
                tallest = heights[i]

        n = len(result)
        for i in range(n // 2):
            result[n-i-1], result[i] = result[i], result[n-i-1]
        
        return result