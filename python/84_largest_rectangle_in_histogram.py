class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        h_stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            if len(h_stack) > 1 and heights[i] < heights[h_stack[-1]]:
                r = h_stack[-1]
                while True:
                    h = heights[h_stack.pop()]
                    max_area = max(max_area, h * (r - h_stack[-1]))
                    if len(h_stack) == 1 or heights[h_stack[-1]] <= heights[i]:
                        break
            h_stack.append(i)

        for i in range(len(h_stack)-1, 0, -1):
            max_area = max(max_area, heights[h_stack[i]] * (h_stack[-1] - h_stack[i-1]))

        return max_area