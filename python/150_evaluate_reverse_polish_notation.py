class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        def operate(op, stack):
            a, b = stack.pop(), stack.pop()
            if op == '+':
                stack.append(b + a)
            elif op == '-':
                stack.append(b - a)
            elif op == '*':
                stack.append(b * a)
            else:
                stack.append(int(b / a))

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                operate(token, stack)
            else:
                stack.append(int(token))
                
        return stack[0]