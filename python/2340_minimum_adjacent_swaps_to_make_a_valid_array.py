class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        min_elem, min_index = math.inf, math.inf
        max_elem, max_index = -math.inf, -math.inf

        for i in range(n):
            if nums[i] < min_elem:
                min_elem = nums[i]
                min_index = i
            if nums[n-i-1] > max_elem:
                max_elem = nums[n-i-1]
                max_index = n-i-1
        
        return min_index + n - max_index - 1 - (0 if min_index <= max_index else 1)