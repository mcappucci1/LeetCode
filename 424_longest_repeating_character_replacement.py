class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        counts = [0] * 26
        longest = 0
        majority = 0
        l = 0

        for r in range(n):
            x = ord(s[r]) - ord('A')
            counts[x] += 1
            if (x == majority) or (counts[x] > counts[majority]):
                majority = x
            else:
                while l < r and (r - l + 1 - counts[majority] > k):
                    y = ord(s[l]) - ord('A')
                    counts[y] -= 1
                    if y == majority:
                        majority = counts.index(max(counts))
                    l += 1
            longest = max(longest, r - l + 1)

        return longest