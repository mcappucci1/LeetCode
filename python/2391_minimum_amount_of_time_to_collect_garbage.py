class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        last_index = [0] * 3
        types = 'GMP'
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
        for i in range(len(garbage)):
            total += len(garbage[i])
            for j in range(3):
                if types[j] in garbage[i]:
                    last_index[j] = i
        for index in last_index:
            if index > 0:
                total += travel[index-1]
        return total