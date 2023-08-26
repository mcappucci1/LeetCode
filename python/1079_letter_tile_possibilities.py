class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        counts = [0 for i in range(26)]
        norm = ord('A')
        for tile in tiles:
            counts[(ord(tile) - norm)] += 1

        def recNumTilePossibilities(counts):
            numAtCount = 0
            for i in range(26):
                if counts[i] > 0:
                    counts[i] -= 1
                    numAtCount += 1 + recNumTilePossibilities(counts)
                    counts[i] += 1
            return numAtCount
        
        return recNumTilePossibilities(counts)