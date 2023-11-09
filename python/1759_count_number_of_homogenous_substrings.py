class Solution:
    def countHomogenous(self, s: str) -> int:
        
        count = 1
        start = 0

        for i in range(1, len(s)):
            if s[i] == s[start]:
                count += i - start + 1
            else:
                start = i
                count += 1
        
        return count % (10 ** 9 + 7)