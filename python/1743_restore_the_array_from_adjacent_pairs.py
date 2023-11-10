class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        n = len(adjacentPairs) + 1
        items = defaultdict(list)
        for i in range(n-1):
            a, b = adjacentPairs[i]
            items[a].append(b)
            items[b].append(a)
        
        first = 0
        for key in items.keys():
            if len(items[key]) == 1:
                first = key
                break
        
        prev = None
        result = [first] + [0] * (n-1)
        for i in range(1, n):
            neighbors = items[first]
            tmp = first
            first = neighbors[0] if prev != neighbors[0] else neighbors[1]
            prev = tmp
            result[i] = first
        return result