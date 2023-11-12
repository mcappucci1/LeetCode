class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        graph = defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].add(i)
        
        if target not in graph:
            return -1
        
        queue = deque()
        seen_stops = set([source])
        seen_routes = [False] * len(routes)
        for route in graph[source]:
            queue.append((route,1))
            seen_routes[route] = True

        while queue:
            curr_route, steps = queue.popleft()
            if curr_route in graph[target]:
                return steps
            for stop in routes[curr_route]:
                if stop not in seen_stops:
                    seen_stops.add(stop)
                    for next_route in graph[stop]:
                        if not seen_routes[next_route]:
                            queue.append((next_route, steps+1))
                            seen_routes[next_route] = True
        
        return -1