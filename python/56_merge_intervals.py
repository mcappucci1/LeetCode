class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        result = []
        curr = intervals[0]

        for i in range(1, len(intervals)):
            if curr[1] >= intervals[i][0]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                result.append(curr)
                curr = intervals[i]
        
        result.append(curr)

        return result