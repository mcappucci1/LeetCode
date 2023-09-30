class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 10 or x % 10 == 0:
            return 0 <= x < 10
        
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return x == reverse or reverse // 10 == x