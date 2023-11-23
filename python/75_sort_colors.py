class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        i = 0
        for num in range(3):
            for j in range(counts[num]):
                nums[i] = num
                i += 1