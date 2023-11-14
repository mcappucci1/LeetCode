class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        m = len(str1)
        n = len(str2)
        
        for i in range(min(m, n), 0, -1):
            if (m % i == 0) and (n % i == 0):
                works = True
                t = str1[:i]
                if (t * (m // i) == str1) and (t * (n // i) == str2):
                    return t
        
        return ''