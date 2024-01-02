class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def recSolve(i, last, count, k, memo):
            if k < 0:
                return math.inf
            elif i == len(s):
                return 0
            elif (i, last, count, k) in memo:
                return memo[(i, last, count, k)]
            delete = recSolve(i+1, last, count, k-1, memo)
            keep = math.inf
            if s[i] == last:
                keep = recSolve(i+1, last, count+1, k, memo) + (count in [1,9,99])
            else:
                keep = recSolve(i+1, s[i], 1, k, memo) + 1
            best = min(delete, keep)
            memo[(i, last, count, k)] = best
            return best


        return recSolve(0, '', 0, k, {})