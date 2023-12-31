class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = []
        for c in s:
            if c == '(' and count > 0:
                result.append(c)
            elif c == ')' and count > 1:
                result.append(c)
            count += 1 if c == '(' else -1
        return ''.join(result)