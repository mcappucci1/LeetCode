class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            return 1 / self.myPow(x, abs(n))

        negative = (x < 0) and (n % 2 == 1)
        exp = 1
        multiplier = abs(x)
        total = 1

        while n > 0:
            if exp > n:
                exp /= 2
                multiplier = sqrt(multiplier)
            else:
                n -= exp
                total *= multiplier
                if n > exp:
                    multiplier *= multiplier
                    exp *= 2
        
        return total * (-1 if negative else 1)