class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        widest = 0
        for i in range(len(points)-1):
            widest = max(widest, points[i+1][0] - points[i][0])
        return widest