class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            curr_water = min(height[left], height[right]) * (right - left)
            most_water = max(most_water, curr_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water