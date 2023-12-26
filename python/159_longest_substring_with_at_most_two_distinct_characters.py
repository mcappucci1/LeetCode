class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        n = len(s)
        longest = 0
        seen = dict()
        l = 0

        for r in range(n):
            seen[s[r]] = r
            if len(seen) > 2:
                longest = max(longest, r - l)
                key = min(seen, key=seen.get)
                l = seen[key] + 1
                del seen[key]

        return max(longest, n - l)