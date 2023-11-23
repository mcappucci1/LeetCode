class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack if k == 0 else stack[:-k]
        return ''.join(stack).lstrip('0') or '0'