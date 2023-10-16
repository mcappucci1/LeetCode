class Solution:
    def makePalindrome(self, s: str) -> bool:
        total_mismatch = 0
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                total_mismatch += 1
                if total_mismatch > 2:
                    return False
            left += 1
            right -= 1
        return True