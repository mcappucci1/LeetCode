class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:

        n = len(arrival)
        result = [0] * n
        entering = deque()
        exiting = deque()
        
        time = arrival[0]
        i = 0
        last_use = [-math.inf, 1]

        while i < n or exiting or entering:
            if (i < n) and (arrival[i] > time) and (not exiting) and (not entering):
                time = arrival[i]

            while i < n and arrival[i] <= time:
                if state[i] == 0:
                    entering.append(i)
                else:
                    exiting.append(i)
                i += 1
            
            if exiting and (last_use[0] < time-1 or last_use[1] == 1 or (not entering)):
                while exiting:
                    x = exiting.popleft()
                    result[x] = time
                    last_use[0] = time
                    time += 1
                last_use[1] = 1
            else:
                while entering:
                    x = entering.popleft()
                    result[x] = time
                    last_use[0] = time
                    time += 1
                last_use[1] = 0

        return result