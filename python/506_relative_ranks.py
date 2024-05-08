class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)
        answer = [None] * n
        indexes = dict()
        
        for i in range(n):
            indexes[score[i]] = i
        
        score = sorted(score, reverse=True)
        for i in range(n):
            if i > 2:
                answer[indexes[score[i]]] = str(i+1)
            elif i == 0:
                answer[indexes[score[i]]] = "Gold Medal"
            elif i == 1:
                answer[indexes[score[i]]] = "Silver Medal"
            else:
                answer[indexes[score[i]]] = "Bronze Medal"
        
        return answer