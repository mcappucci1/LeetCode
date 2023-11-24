class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []

        n = len(nums)
        ranges = []
        start = 0

        def rangeStr(s, e):
            return str(nums[s]) if s == e else (str(nums[s]) + '->' + str(nums[e]))

        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                ranges.append(rangeStr(start, i-1))
                start = i
                
        ranges.append(rangeStr(start, n-1))
        return ranges