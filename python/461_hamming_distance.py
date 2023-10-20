class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        total = 0
        while diff != 0:
            total += diff % 2
            diff >>= 1
        return total