class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        left_to_right = nums[0]
        right_to_left = nums[-1]

        for i in range(1, n):
            answer[i] *= left_to_right
            left_to_right *= nums[i]
            answer[n-i-1] *= right_to_left
            right_to_left *= nums[n-i-1]

        return answer