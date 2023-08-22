class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        total_provinces = 0
        seen = set()
        n = len(isConnected)

        for i in range(n):
            if i in seen:
                continue
            total_provinces += 1
            seen.add(i)
            stack = [i]
            while stack:
                curr = stack.pop()
                for j in range(n):
                    if isConnected[curr][j] == 0 or j in seen:
                        continue
                    seen.add(j)
                    stack.append(j)

        return total_provinces