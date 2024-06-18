class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)

        l, r = 0, len(warehouse) - 1
        i = 0
        total = 0

        while l <= r and i < len(boxes):
            if boxes[i] <= warehouse[l] or boxes[i] <= warehouse[r]:
                total += 1
                if warehouse[l] > warehouse[r]:
                    l += 1
                else:
                    r -= 1
            i += 1
        
        return total