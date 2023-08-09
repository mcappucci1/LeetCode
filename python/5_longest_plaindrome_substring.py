class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        def findLongestPalindrome(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        longest = ""

        for i in range(n):
            one = findLongestPalindrome(i, i)
            two = findLongestPalindrome(i, i + 1)
            longest = longest if len(longest) > len(one) else one
            longest = longest if len(longest) > len(two) else two

        return longest