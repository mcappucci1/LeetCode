class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        orig = True
        index = k
        length = pow(2, n-1)

        while index != 1:
            if index > length // 2:
                index -= length // 2
                orig = not orig
            length //= 2

        return int(not orig)