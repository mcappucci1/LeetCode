class Solution:
    def numberOfWays(self, corridor: str) -> int:

        seats = 0
        end_point = len(corridor)-1
        while seats < 2 and end_point >= 0:
            if corridor[end_point] == 'S':
                seats += 1
            end_point -= 1
        end_point += 1
        
        if seats < 2: return 0
        
        total = 1
        prev = 1
        seats = 0

        for i in range(end_point):
            if corridor[i] == 'S':
                seats += 1
                if seats % 2 == 1 and seats > 1:
                    prev = total
            elif seats and seats % 2 == 0:
                total += prev
        
        if seats % 2 == 1:
            return 0
        return total % (pow(10, 9) + 7)