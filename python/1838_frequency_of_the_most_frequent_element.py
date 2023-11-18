class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()
        l, r = 0, 0
        max_freq = 0
        total = 0
        prev = nums[0]

        while r < n:
            elem = nums[r]
            count = 1
            while (r+count) < n and nums[r+count] == elem:
                count += 1
            total += (elem - prev) * (r - l)
            while total > k:
                total -= elem - nums[l]
                l += 1
            max_freq = max(max_freq, count + (r-l))
            prev = elem
            r += count
        
        return max_freq