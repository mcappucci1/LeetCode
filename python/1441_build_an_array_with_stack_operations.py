class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack_operations = []
        target_index = 0
        for stream_elem in range(1, target[-1] + 1):
            stack_operations.append('Push')
            if stream_elem == target[target_index]:
                target_index += 1
            else:
                stack_operations.append('Pop')
        return stack_operations