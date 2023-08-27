class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.items = []

    def insert(self, val: int) -> bool:
        not_contains = val not in self.map
        if not_contains:
            self.map[val] = len(self.items)
            self.items.append(val)
        return not_contains

    def remove(self, val: int) -> bool:
        contains = val in self.map
        if contains:
            self.map[self.items[len(self.items) - 1]] = self.map[val]
            self.items[self.map[val]] = self.items[-1]
            self.items.pop()
            del self.map[val]
        return contains

    def getRandom(self) -> int:
        return self.items[random.randint(0, len(self.items) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()