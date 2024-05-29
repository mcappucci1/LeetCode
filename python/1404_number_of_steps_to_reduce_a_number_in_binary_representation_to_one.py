class Solution:
    def numSteps(self, s: str) -> int:

        s = deque(s)
        steps = 0

        while len(s) > 1:
            steps += 1
            if s[-1] == '0':
                s.pop()
            else:
                carry, s[-1] = True, '0'
                for i in range(len(s)-2, -1, -1):
                    s[i] = '0' if s[i] == '1' else '1'
                    carry = s[i] == '0'
                    if (not carry):
                        break
                if carry:
                    s.appendleft('1')
        
        return steps