class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        n = len(arr)
        counts = [0] * (n+1)
        
        for num in arr:
            counts[min(n, num)] += 1

        largest = 1
        for i in range(1, n+1):
            largest = min(i, largest + counts[i])

        return largest