class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        min_end = points[0][1]
        total_arrows = 1

        for i in range(1, len(points)):
            if points[i][0] > min_end:
                total_arrows += 1
                min_end = inf
            min_end = min(min_end, points[i][1])

        return total_arrows