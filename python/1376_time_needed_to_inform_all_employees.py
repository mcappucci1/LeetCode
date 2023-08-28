class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        tree = defaultdict(list)
        for i in range(n):
            if i == headID:
                continue
            tree[manager[i]].append(i)
        
        max_mins = informTime[headID]
        stack = [(headID, informTime[headID])]
        while stack:
            (employee, time) = stack.pop()
            max_mins = max(max_mins, time)
            for subordinate in tree[employee]:
                stack.append((subordinate, time + informTime[subordinate]))
        return max_mins