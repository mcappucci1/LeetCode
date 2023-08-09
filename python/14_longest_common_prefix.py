class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find smallest string in array
        shortest_string = min(strs, key=len)

        # Find the smallest prefix
        for i in range(len(shortest_string)):
            for other_string in strs:
                if shortest_string[i] != other_string[i]:
                    return shortest_string[:i]
        return shortest_string