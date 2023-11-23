class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        m = len(l)
        result = [False] * m
        for i in range(m):
            if r[i] - l[i] < 1:
                continue
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            arith = arr[1] - arr[0]
            valid = True
            for j in range(2, len(arr)):
                if arr[j] - arr[j-1] != arith:
                    valid = False
                    break
            if valid:
                result[i] = True
        return result