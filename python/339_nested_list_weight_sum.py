class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0
        q = deque([nestedList])
        level = 1

        while q:
            l = len(q)
            for i in range(l):
                for e in q.popleft():
                    if e.isInteger():
                        total += e.getInteger() * level
                    else:
                        q.append(e.getList())
            level += 1
        
        return total