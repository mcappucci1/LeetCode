class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:        
        end = True
        streak = 0
        longest = 0
        for seat in seats:
            if seat == 0:
                streak += 1
            else:
                longest = max(longest, streak if end else math.ceil(streak / 2))
                streak = 0
                end = False
        return max(longest, streak)
