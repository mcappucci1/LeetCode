class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = [[]]
        
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                arr = stack.pop()
                arr = arr if len(stack) % 2 == 0 else arr[::-1]
                stack[-1].append(arr)
            else:
                stack[-1].append(c)

        def flatten(stack, result):
            for elem in stack:
                if type(elem) == list:
                    flatten(elem, result)
                else:
                    result.append(elem)
            return result
        
        return ''.join(flatten(stack, []))