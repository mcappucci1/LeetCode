class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        total = 0
        l = 0
        r = len(nums)-1

        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] < nums[r]:
                total += 1
                nums[l+1] += nums[l]
                l += 1
            else:
                total += 1
                nums[r-1] += nums[r]
                r -= 1
        
        return total