class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        m, n = len(version1), len(version2)
        i, j = 0, 0
        
        while i < m or j < n:
            val1 = int(version1[i]) if i < m else 0
            val2 = int(version2[i]) if j < n else 0
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
            i += 1
            j += 1
        
        return 0