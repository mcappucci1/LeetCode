class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:

        n = len(nums)
        best = [0] + [math.inf] * (n - 1)
        inc = [0]
        dec = [0]

        for i in range(1, n):
            best[i] = best[i-1] + costs[i]
            if nums[i-1] > nums[i]:
                while dec and nums[dec[-1]] > nums[i]:
                    best[i] = min(best[i], best[dec.pop()] + costs[i])
            else:
                while inc and nums[inc[-1]] <= nums[i]:
                    best[i] = min(best[i], best[inc.pop()] + costs[i])
            inc.append(i)
            dec.append(i)
        
        return best[-1]