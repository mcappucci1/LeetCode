class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        sum_of_m = sum(rolls)
        total = (len(rolls) + n) * mean

        remaining_total = total - sum_of_m

        if (remaining_total / n > 6) or (remaining_total / n < 1):
            return []
        
        k = remaining_total % n
        n_rolls = [remaining_total // n] * n

        for i in range(k):
            n_rolls[i] += 1
        
        return n_rolls