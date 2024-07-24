class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def cmp(a):
            if a == 0:
                return mapping[a]
            total, mult = 0, 1
            while a:
                total += mapping[a % 10] * mult
                mult *= 10
                a //= 10
            return total

        nums.sort(key=cmp)
        return nums