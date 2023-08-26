class Solution:
    def fib(self, n: int) -> int:
        one, two = 1, 0
        for i in range(n):
            two, one = one, one + two
        return two