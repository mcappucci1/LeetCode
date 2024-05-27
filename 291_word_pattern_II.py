class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def recMatch(s, p, i, j, m):
            if (i == len(s)) or (j == len(p)):
                return (i == len(s)) and (j == len(p))
            x = ord(p[j]) - ord('a')
            if m[x] != None:
                l = len(m[x])
                if l > (len(s) - i) or s[i:i+l] != m[x]:
                    return False
                return recMatch(s, p, i + l, j + 1, m)
            else:
                for k in range(i, len(s) - (len(p) - j - 1)):
                    sub = s[i:k+1]
                    if sub in m:
                        continue
                    m[x] = sub
                    if recMatch(s, p, k+1, j+1, m):
                        m[x] = None
                        return True
                m[x] = None
            
            return False

        return recMatch(s, pattern, 0, 0, [None] * 26)