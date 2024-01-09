class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        count = 0
        total = 0

        vals = defaultdict(int)
        vals[0] += 1
        
        for i in range(n):
            total += nums[i]
            count += vals[total - k]
            vals[total] += 1
            
        return count