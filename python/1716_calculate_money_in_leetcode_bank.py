class Solution:
    def totalMoney(self, n: int) -> int:
        r = n % 7
        weeks = n // 7
        return 28 * weeks + 7 * weeks * (weeks-1) // 2 + r * (r+1) // 2 + weeks * r