class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_val = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[last_val] = nums[i]
                last_val += 1
        return last_val