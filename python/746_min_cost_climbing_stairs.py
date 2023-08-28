class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step_back = cost[1]
        two_steps_back = cost[0]
        for i in range(2, len(cost)):
            tmp = one_step_back
            one_step_back = cost[i] + min(one_step_back, two_steps_back)
            two_steps_back = tmp
        return min(one_step_back, two_steps_back)