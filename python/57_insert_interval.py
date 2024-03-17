class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        i, j = 0, n-1

        while i <= j:
            m = (j + i) // 2
            if intervals[m][1] < newInterval[0]:
                i = m + 1
            else:
                j = m - 1

        merged = intervals[:i]
        
        while i < n and ((intervals[i][1] >= newInterval[0]) and (newInterval[1] >= intervals[i][0])):
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        
        return merged + [newInterval] + intervals[i:]