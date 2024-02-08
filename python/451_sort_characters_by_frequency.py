class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        s = ''
        for c, count in counts:
            s += c * count
        return s