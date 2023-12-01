class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        total = 0
        matching_pairs = dict()
        for a, b in dominoes:
            pair = (a,b) if a < b else (b,a)
            if pair not in matching_pairs:
                matching_pairs[pair] = 1
            else:
                total += matching_pairs[pair]
                matching_pairs[pair] += 1
        return total