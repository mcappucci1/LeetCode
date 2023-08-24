class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_x = 0
        tmp = x
        while tmp > 0:
            reverse_x = reverse_x * 10 + tmp % 10
            tmp //= 10
        
        return x == reverse_x