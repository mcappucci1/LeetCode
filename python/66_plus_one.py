class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i > -1 and carry:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1
        if carry:
            digits.insert(0, 1)
        return digits