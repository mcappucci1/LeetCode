class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[0, []] for i in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course][0] += 1
            graph[prereq][1].append(course)
        
        topological_sort = []
        q = deque()

        for course in range(numCourses):
            if graph[course][0] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            topological_sort.append(course)
            for neighbor in graph[course][1]:
                graph[neighbor][0] -= 1
                if graph[neighbor][0] == 0:
                    q.append(neighbor)
        
        return topological_sort if len(topological_sort) == numCourses else []
