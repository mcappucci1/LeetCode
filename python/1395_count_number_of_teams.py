class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        num_teams = 0
        desc = [0] * n
        asc = [0] * n
        
        for i in range(1, n):
            total = 0
            for j in range(i-1, -1, -1):
                if rating[i] > rating[j]:
                    asc[i] += 1
                    num_teams += asc[j]
                else:
                    desc[i] += 1
                    num_teams += desc[j]
        
        return num_teams