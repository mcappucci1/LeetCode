class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        n = len(colors)
        l = 0
        min_time = 0
        total = neededTime[0]
        most = neededTime[0]

        for r in range(1, n):
            if colors[r] != colors[l]:
                min_time += total - most
                total, most = 0, 0
                l = r
            total += neededTime[r]
            most = max(most, neededTime[r])

        if l != n - 1:
            min_time += total - most

        return min_time