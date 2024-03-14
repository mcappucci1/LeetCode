class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        result = 0
        count = 0
        counts = defaultdict(int)
        counts[0] = 1

        for num in nums:
            count += num
            if count >= goal:
                result += counts[count - goal]
            counts[count] += 1
        
        return result