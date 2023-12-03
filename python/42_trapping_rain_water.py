class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = [0]
        total = 0

        for i in range(1, len(height)):
            if height[i] >= height[i-1] and stack:
                base = stack.pop()
                while stack:
                    total += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[base])
                    if height[i] <= height[stack[-1]]:
                        break
                    base = stack.pop()
            stack.append(i)
        
        return total
