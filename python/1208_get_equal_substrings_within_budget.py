class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        longest = 0
        l = 0

        for r in range(len(s)):
            maxCost -= abs(ord(s[r]) - ord(t[r]))
            while maxCost < 0 and l <= r:
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1
            longest = max(longest, r - l + 1)

        return longest