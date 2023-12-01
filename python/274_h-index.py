class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        counts = [0] * (n+1)

        for citation in citations:
            counts[min(citation, n)] += 1

        best_h = n
        total = counts[n]

        while best_h > total:
            best_h -= 1
            total += counts[best_h]

        return best_h