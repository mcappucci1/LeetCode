class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        stack = [0]
        seen = [False] * len(rooms)
        seen[0] = True

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not seen[key]:
                    stack.append(key)
                    seen[key] = True

        return False not in seen