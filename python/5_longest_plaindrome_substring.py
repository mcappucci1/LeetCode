class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        longest = (0,0)

        def palLength(l, r):
            nonlocal longest
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 2) > (longest[1] - longest[0]):
                longest = (l+1, r-1)

        for i in range(n-1):
            palLength(i, i)
            palLength(i, i+1)

        return s[longest[0]:longest[1]+1]