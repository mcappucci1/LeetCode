class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total_substrings = 0
        count = 0
        for c in s:
            count += -1 if c == 'L' else 1
            if count == 0:
                total_substrings += 1
        return total_substrings