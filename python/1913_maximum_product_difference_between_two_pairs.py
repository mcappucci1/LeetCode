class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        most, second_most = -math.inf, -math.inf
        least, second_least = math.inf, math.inf
        for num in nums:
            if num > second_most:
                tmp = min(most, num)
                most = max(most, num)
                second_most = tmp
            if num < second_least:
                tmp = max(least, num)
                least = min(least, num)
                second_least = tmp
        return (most * second_most) - (least * second_least)