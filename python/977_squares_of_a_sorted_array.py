class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l = 0
        r = n - 1
        squares = [0] * n

        for i in range(n-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                squares[i] = nums[l] * nums[l]
                l += 1
            else:
                squares[i] = nums[r] * nums[r]
                r -= 1
        
        return squares