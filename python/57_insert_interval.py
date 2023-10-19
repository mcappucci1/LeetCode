class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0 or intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals

        def overlap(a, b):
            return (a[0] <= b[1]) and (b[0] <= a[1])

        lo, hi = 0, len(intervals) - 1
        while lo <= hi:
            m = (hi + lo) // 2
            if intervals[m][1] < newInterval[0]:
                lo  = m + 1
            elif newInterval[1] < intervals[m][0] or overlap(newInterval, intervals[m]):
                hi = m - 1

        j = lo
        while j < len(intervals) and overlap(newInterval, intervals[j]):
            newInterval[0] = min(newInterval[0], intervals[j][0])
            newInterval[1] = max(newInterval[1], intervals[j][1])
            j += 1
        
        return intervals[:lo] + [newInterval] + intervals[j:]