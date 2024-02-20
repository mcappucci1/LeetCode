class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        n = len(arr)

        if arr[-1] - n < k:
            return arr[-1] + (k - arr[-1] + n)
        
        lo, hi = 0, n-1
        while lo <= hi:
            m = (lo + hi) // 2
            miss = arr[m] - (m+1)
            if miss >= k:
                hi = m - 1
            elif miss < k:
                lo = m + 1
                
        return lo + k