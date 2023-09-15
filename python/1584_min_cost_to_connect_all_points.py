class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        total_cost = 0
        costs = [float('inf')] * n
        curr = 0

        for x in range(n-1):
            global_min, index = float('inf'), -1
            for i in range(n):
                if i != curr and costs[i] >= 0:
                    dist = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    costs[i] = min(costs[i], dist)
                    if costs[i] < global_min:
                        global_min = costs[i]
                        index = i
            costs[curr] *= -1
            curr = index
            total_cost += global_min
        
        return total_cost