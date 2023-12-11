class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:        
        n = len(arr)
        l = 0
        for i in range(1, n):
            if arr[i] != arr[i-1]:
                if i - l > n / 4:
                    return arr[i-1]
                l = i
        return arr[-1]