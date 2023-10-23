class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        counts = [0] * (max_val - min_val + 1)
        for num in nums:
            counts[num - min_val] += 1
        for i in range(len(counts)-1, -1, -1):
            k -= counts[i]
            if k <= 0:
                return i + min_val