class Solution:
    def isValid(self, s: str) -> bool:
        parens = { '(': ')', '{': '}', '[': ']' }
        stack = []
        for c in s:
            if c in parens:
                stack.append(c)
            else:
                if (not stack) or (parens[stack[-1]] != c):
                    return False
                stack.pop()
        return not stack