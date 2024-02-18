class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        rooms = [i for i in range(n)]
        curr = []
        counts = [0] * n
        meetings.sort()

        i = 0
        time = 0
        while i < len(meetings):
            time = max(time, meetings[i][0])
            while curr and curr[0][0] <= meetings[i][0]:
                room = heapq.heappop(curr)[1]
                heapq.heappush(rooms, room)
            if rooms:
                room = heapq.heappop(rooms)
                counts[room] += 1
                heapq.heappush(curr, (meetings[i][1] + (time - meetings[i][0]), room))
                i += 1
            else:
                time = curr[0][0]
                while curr and curr[0][0] == time:
                    room = heapq.heappop(curr)[1]
                    heapq.heappush(rooms, room)

        max_count = 0
        min_room = inf
        for i in range(n):
            if counts[i] > max_count:
                min_room = i
                max_count = counts[i]
        
        return min_room