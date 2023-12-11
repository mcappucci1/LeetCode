class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Store the letters in an array, array will store placement of the char
        # iterate over all chars
        # Iterate over all wor
        
        chars = [0] * 26
        norm = ord('a')
        for i in range(26):
            chars[ord(order[i]) - norm] = i
        
        for i in range(1, len(words)):
            equal = True
            for j in range(min(len(words[i]), len(words[i-1]))):
                if chars[ord(words[i-1][j]) - norm] < chars[ord(words[i][j]) - norm]:
                    equal = False
                    break
                elif chars[ord(words[i-1][j]) - norm] > chars[ord(words[i][j]) - norm]:
                    return False
            if equal and (len(words[i-1]) > len(words[i])):
                return False
        
        return True