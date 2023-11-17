class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        
        peaks.sort(key=lambda peak: peak[0] - peak[1])

        num_visible = 1
        rightmost_peak = peaks[0]
        same = False

        for i in range(1, len(peaks)):
            p = peaks[i]
            if rightmost_peak[0] == p[0] and rightmost_peak[1] == p[1]:
                if not same:
                    num_visible -= 1
                    same = True
            elif p[1] - abs(p[0] - rightmost_peak[0]) >= rightmost_peak[1]:
                same = False
                rightmost_peak = p
            elif rightmost_peak[1] - abs(p[0] - rightmost_peak[0]) < p[1]:
                same = False
                rightmost_peak = p
                num_visible += 1

        return num_visible