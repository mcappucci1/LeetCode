class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        first = [-1] * 26
        last = [-1] * 26
        
        for i in range(len(s)):
            x = ord(s[i]) - ord('a')
            if first[x] == -1:
                first[x] = i
            else:
                last[x] = i
        
        intervals = [[first[i], last[i]] for i in range(26) if last[i] != -1]
        
        if not intervals:
            return [1] * len(s)
        
        intervals.sort(key=lambda elem: elem[0])
        result = [1] * intervals[0][0]
        interval = intervals[0]
        
        for i in range(1, len(intervals)):
            if interval[1] < intervals[i][0]:
                result.append(interval[1] - interval[0] + 1)
                result.extend([1] * (intervals[i][0] - interval[1] - 1))
                interval = intervals[i]
            else:
                interval[1] = max(interval[1], intervals[i][1])
        result.append(interval[1] - interval[0] + 1)
        result.extend([1] * (len(s) - interval[1] - 1))
        
        return result