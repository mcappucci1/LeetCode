class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        best = 0
        curr = 0
        l, r = 0, len(tokens)-1

        tokens.sort()

        while l <= r and (power >= tokens[l] or curr > 0):
            if power >= tokens[l]:
                curr += 1
                power -= tokens[l]
                l += 1
                best = max(best, curr)
            elif curr > 0:
                power += tokens[r]
                r -= 1
                curr -= 1
        
        return best