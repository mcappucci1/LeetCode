class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        s = list(s)
        count = 0
        l = 0

        for r in range(len(s)):
            s[l] = s[r]
            if s[l] == '(':
                count += 1
            elif s[l] == ')':
                if count == 0:
                    l -= 1
                else:
                    count -= 1
            l += 1
        
        i = l-1
        while count > 0 and i > -1:
            if s[i] == '(':
                count -= 1
                s[i] = ''
            i -= 1
        
        return ''.join(s[:l])