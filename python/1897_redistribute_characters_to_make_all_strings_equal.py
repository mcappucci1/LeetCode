class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        n = len(words)
        counts = [0] * 26
        norm = ord('a')

        for word in words:
            for c in word:
                counts[ord(c) - norm] += 1
        
        for count in counts:
            if count % n != 0:
                return False
        
        return True