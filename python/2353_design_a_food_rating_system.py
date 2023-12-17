class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisine = dict()
        self.foodToScore = dict()
        self.cuisineToHeap = defaultdict(list)
        
        for i in range(len(foods)):
            self.foodToCuisine[foods[i]] = cuisines[i]
            self.foodToScore[foods[i]] = -ratings[i]
            heapq.heappush(self.cuisineToHeap[cuisines[i]], (-ratings[i], foods[i]))


    def changeRating(self, food: str, newRating: int) -> None:
        self.foodToScore[food] = -newRating
        heapq.heappush(self.cuisineToHeap[self.foodToCuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineToHeap[cuisine]
        while heap[0][0] != self.foodToScore[heap[0][1]]:
            heapq.heappop(heap)
        return heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)