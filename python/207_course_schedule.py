class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        degree = [0] * numCourses
        nextCourses = [[] for i in range(numCourses)]
        
        for [a, b] in prerequisites:
            nextCourses[a].append(b)
            degree[b] += 1
        
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        completeCount = 0

        while queue:
            completeCount += 1
            course = queue.popleft()
            for nextCourse in nextCourses[course]:
                degree[nextCourse] -= 1
                if degree[nextCourse] == 0:
                    queue.append(nextCourse)

        return completeCount == numCourses