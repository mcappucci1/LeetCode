class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        remainder = 0
        while numBottles:
            total += numBottles
            numBottles += remainder
            remainder = numBottles % numExchange
            numBottles = numBottles // numExchange
        return total