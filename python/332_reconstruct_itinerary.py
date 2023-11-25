class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        total_flights = len(tickets)
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)

        for city in graph:
            graph[city].sort(reverse=True)
        
        def backtrack(graph, city, num_flights):
            if num_flights == total_flights:
                return [None] * total_flights + [city]
            for next_city in graph[city]:
                if graph[city][next_city] > 0:
                    graph[city][next_city] -= 1
                    cities = backtrack(graph, next_city, num_flights+1)
                    if cities:
                        cities[num_flights] = city
                        return cities
                    graph[city][next_city] += 1
            return None

        return backtrack(graph, 'JFK', 0)