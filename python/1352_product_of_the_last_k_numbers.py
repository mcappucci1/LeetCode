class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k: int) -> int:
        if k >= len(self.arr):
            return 0
        else:
            return self.arr[-1] // self.arr[len(self.arr)-k-1]