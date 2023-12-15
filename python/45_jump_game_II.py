class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        total_jumps = 0
        next_furthest = 0
        end_of_range = 0
        
        for i in range(n - 1):
            next_furthest = max(i + nums[i], next_furthest)
            if i == end_of_range:
                end_of_range = next_furthest
                total_jumps += 1
        
        return total_jumps