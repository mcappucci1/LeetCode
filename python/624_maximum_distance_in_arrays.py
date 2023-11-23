class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        small = [(math.inf, -1), (math.inf, -1)]
        large = [(math.inf, -1), (math.inf, -1)]
        
        for i in range(len(arrays)):
            if arrays[i][0] < small[-1][0]:
                small.pop()
                heapq.heappush(small, (arrays[i][0], i))
            if -arrays[i][-1] < large[-1][0]:
                large.pop()
                heapq.heappush(large, (-arrays[i][-1], i))
        
        if small[0][1] == large[0][1]:
            return max(abs(-large[0][0] - small[1][0]), abs(-large[1][0] - small[0][0]))
        return abs(-large[0][0] - small[0][0])