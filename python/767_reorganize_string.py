class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(counts)

        max_letter = 0
        start_letter = ''

        for (count, char) in counts:
            if -count > max_letter:
                max_letter = -count
                start_letter = char

        if max_letter >= len(s) / 2 + 1:
            return ''
        
        result = [''] * len(s)
        index = 0
        for i in range(max_letter):
            result[index] = start_letter
            index += 2
        
        heapq.heappop(counts)
        
        while counts:
            (count, char) = heapq.heappop(counts)
            for i in range(-count):
                if index >= len(result):
                    index = 1
                result[index] = char
                index += 2
        
        return ''.join(result)