class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n

        l, r = 1, 1

        for i in range(n):
            answer[i] *= l
            answer[n-i-1] *= r
            l *= nums[i]
            r *= nums[n-i-1]
        
        return answer