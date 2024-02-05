class Solution:
    def firstUniqChar(self, s: str) -> int:

        n = len(s)
        chars = [n] * 26
        norm = ord('a')

        for i in range(n - 1, -1, -1):
            j = ord(s[i]) - norm
            if chars[j] == n:
                chars[j] = i
            else:
                chars[j] = n+1
        
        x = min(chars)
        return x if x < n else -1