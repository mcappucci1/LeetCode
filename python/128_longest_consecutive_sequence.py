class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union = set(nums)
        longest = 0
        for num in union:
            if num-1 not in union:
                total = 0
                while num in union:
                    total += 1
                    num += 1
                longest = max(longest, total)
        return longest