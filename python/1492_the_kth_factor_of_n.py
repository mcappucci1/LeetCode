class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        factors = []
        root = sqrt(n)
        
        for i in range(1, floor(root) + 1):
            if n % i == 0:
                if k == 1:
                    return i
                k -= 1
                if i != root:
                    factors.append(i)
        
        if len(factors) >= k:
            return n // factors[-k]
        
        return -1