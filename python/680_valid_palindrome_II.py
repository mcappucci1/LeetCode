class Solution:
    def validPalindrome(self, s: str) -> bool:

        def matching(s, l, r, d):
            while l < r:
                if s[l] != s[r]:
                    return False if d else (matching(s, l+1, r, True) or matching(s, l, r-1, True))
                l += 1
                r -= 1
            return True
        
        return matching(s, 0, len(s)-1, False)