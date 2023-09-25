class Solution:

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


    def partition(self, arr, lo, hi):
        smaller = lo
        for i in range(lo, hi):
            if arr[i][1] < arr[hi][1]:
                self.swap(arr, i, smaller)
                smaller += 1
        if smaller < hi:
            self.swap(arr, smaller, hi)
        return smaller


    def quickSelect(self, arr, lo, hi, k):
        # Base case, lo >= hi
        if lo >= hi:
            return

        # Select a pivot
        pivot = random.randint(lo, hi)
        self.swap(arr, pivot, hi)

        # Parition the aray based on the value of that pivot
        part_index = self.partition(arr, lo, hi)

        # Recurse on the half of the array that contains target k
        if part_index < k:
            self.quickSelect(arr, part_index + 1, hi, k)
        elif part_index > k:
            self.quickSelect(arr, lo, part_index - 1, k)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums = list(Counter(nums).items())
        n = len(nums)
        self.quickSelect(nums, 0, n-1, n-k)
        return [entry[0] for entry in nums[n-k:]]