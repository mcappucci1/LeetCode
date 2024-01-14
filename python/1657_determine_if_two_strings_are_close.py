class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26
        seen1 = 0
        seen2 = 0
        norm = ord('a')

        for i in range(len(word1)):
            count1[ord(word1[i]) - norm] += 1
            count2[ord(word2[i]) - norm] += 1
            seen1 |= 1 << ord(word1[i])
            seen2 |= 1 << ord(word2[i])

        if seen1 != seen2:
            return False
        
        count1.sort()
        count2.sort()

        for i in range(26):
            if count1[i] != count2[i]:
                return False
        
        return True