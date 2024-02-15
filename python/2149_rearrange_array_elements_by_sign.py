class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0] * n
        pos, neg = 0, 0

        for i in range(0, n, 2):
            while nums[pos] < 0: pos += 1
            while nums[neg] > 0: neg += 1
            result[i] = nums[pos]
            result[i+1] = nums[neg]
            pos += 1
            neg += 1

        return result