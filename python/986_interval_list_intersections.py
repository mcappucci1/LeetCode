class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        intersection = []
        m, n = len(firstList), len(secondList)
        i, j = 0, 0

        while (i < m) and (j < n):
            if (firstList[i][0] <= secondList[j][1]) and (secondList[j][0] <= firstList[i][1]):
                intersection.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return intersection