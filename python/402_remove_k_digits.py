class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i = 0
        while i < len(num):
            if stack and int(stack[-1]) > int(num[i]):
                stack.pop()
                k -= 1
                if k == 0:
                    break
                i -= 1
            else:
                stack.append(num[i])
            i += 1
        while k > 0 and stack:
            stack.pop()
            k -= 1
        s = ''.join(stack) + num[i:]
        i = 0
        while i < len(s)-1 and s[i] == '0':
            i += 1
        s = s[i:]
        return s or '0'