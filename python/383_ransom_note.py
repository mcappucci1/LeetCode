class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        norm = ord('a')
        counts = [0 for i in range(26)]
        for letter in ransomNote:
            counts[ord(letter) - norm] += 1
        for letter in magazine:
            counts[ord(letter) - norm] -= 1
        for count in counts:
            if count > 0:
                return False
        return True