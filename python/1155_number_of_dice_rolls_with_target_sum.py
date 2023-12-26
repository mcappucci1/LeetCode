class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        memo = [0] * (target+1)
        memo[0] = 1

        for roll in range(1, n+1):
            for val in range(target, -1, -1):
                if memo[val] > 0:
                    for roll_val in range(1, k+1):
                        if val + roll_val > target:
                            break
                        memo[val + roll_val] += memo[val]
                memo[val] = 0
        
        return memo[-1] % (pow(10, 9) + 7)