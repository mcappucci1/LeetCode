class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        total = 0
        values = defaultdict(int)
        for i in range(len(nums)):
            rev, num = 0, nums[i]
            while num > 0:
                rev = rev * 10 + (num % 10)
                num //= 10
            total += values[nums[i] - rev]
            values[nums[i] - rev] += 1
        
        return total % (pow(10, 9) + 7)