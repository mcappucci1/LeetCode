class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def recPartition(s, i, j, p, ps):
            if s[i:j+1] == s[i:j+1][::-1]:
                p.append(s[i:j+1])
                if j == len(s)-1:
                    ps.append(p.copy())
                else:
                    recPartition(s, j+1, j+1, p, ps)
                p.pop()
            if j < len(s)-1:
                recPartition(s, i, j+1, p, ps)
            return ps
        
        return recPartition(s, 0, 0, [], [])