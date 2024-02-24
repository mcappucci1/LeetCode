class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        times = defaultdict(lambda: defaultdict(list))
        for x, y, time in meetings:
            t = times[time]
            t[x].append(y)
            t[y].append(x)
        
        count = 2
        hasSecret = [False] * n
        hasSecret[0] = True
        hasSecret[firstPerson] = True

        sortedTimes = sorted(times.keys())

        i = 0
        while count < n and i < len(sortedTimes):
            time = sortedTimes[i]
            stack = [key for key in times[time].keys() if hasSecret[key]]
            while stack:
                x = stack.pop()
                for y in times[time][x]:
                    if not hasSecret[y]:
                        count += 1
                        hasSecret[y] = True
                        stack.append(y)
            i += 1

        return [i for i in range(n) if hasSecret[i]]