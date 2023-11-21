class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        while b:
            total = a ^ b
            carry = (a & b) << 1
            a = total
            b = carry
        return bin(a)[2:]