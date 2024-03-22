class Solution:
    def removeVowels(self, s: str) -> str:

        arr = []
        skip = ['a','e','i','o','u']

        for c in s:
            if c not in skip:
                arr.append(c)

        return ''.join(arr)