class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, lo, hi):
            pivot = nums[hi]
            smaller = lo
            for i in range(lo, hi):
                if nums[i] <= pivot:
                    nums[i], nums[smaller] = nums[smaller], nums[i]
                    smaller += 1
            nums[hi], nums[smaller] = nums[smaller], nums[hi]
            kth = len(nums) - k
            if smaller < kth:
                return quickSelect(nums, smaller + 1, hi)
            elif smaller > kth:
                return quickSelect(nums, lo, smaller - 1)
            return nums[smaller]

        return quickSelect(nums, 0, len(nums) - 1)