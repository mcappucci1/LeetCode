class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        xor = pref[0]
        for i in range(1, len(pref)):
            pref[i] = xor ^ pref[i]
            xor ^= pref[i]
        return pref