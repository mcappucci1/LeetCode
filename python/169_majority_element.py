class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        element = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == element:
                count += 1
            else:
                count -= 1
                if count == 0:
                    element = nums[i]
                    count = 1

        return element