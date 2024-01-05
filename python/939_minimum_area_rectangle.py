class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        min_area = math.inf
        seen = set()

        for x, y in points:
            seen.add((x,y))

        for x1, y1 in points:
            for x2, y2 in points:
                if (x1 > x2) and (y1 > y2) and ((x1, y2) in seen) and ((x2, y1) in seen):
                    min_area = min(min_area, (x1 - x2) * (y1 - y2))

        return 0 if min_area == math.inf else min_area