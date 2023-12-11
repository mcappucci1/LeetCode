class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def keyer(log):
            splitter = log.index(' ')
            if log[splitter + 1].isnumeric():
                return (1,None,None)
            return (0, log[splitter+1:], log[:splitter])

        return sorted(logs, key=keyer)