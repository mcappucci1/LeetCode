class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        max_area = 0
        prev_heights = []

        for row in range(m):
            
            heights = []
            seen = [False] * n
            
            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height+1, col))
                    seen[col] = True
            
            for col in range(n):
                if not seen[col] and matrix[row][col] == 1:
                    heights.append((1, col))
            
            for i in range(len(heights)):
                max_area = max(max_area, heights[i][0] * (i+1))

            prev_heights = heights
            
        return max_area