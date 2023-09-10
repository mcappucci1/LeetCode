class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if (nums[0] <= target < nums[mid]) or (target < nums[mid] < nums[0]) or (nums[mid] < nums[0] <= target):
                hi = mid - 1
            elif (nums[0] <= nums[mid] < target) or (nums[mid] < target < nums[0]) or (target < nums[0] <= nums[mid]):
                lo = mid + 1
            elif nums[mid] == target:
                return mid
        return -1