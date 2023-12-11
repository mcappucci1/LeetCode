class Solution:
    def isHappy(self, n: int) -> bool:

        slow, fast = n, n

        def sqrSum(i):
            total = 0
            while i > 0:
                total += pow((i % 10), 2)
                i //= 10
            return total

        while fast > 1:
            fast = sqrSum(sqrSum(fast))
            slow = sqrSum(slow)
            if fast == slow:
                break

        return fast == 1