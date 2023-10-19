class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        root = 0
        children = set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i
                break

        seen = set([root])
        stack = [root]

        while stack:
            node = stack.pop()
            if leftChild[node] != -1:
                if leftChild[node] in seen:
                    return False
                seen.add(leftChild[node])
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                if rightChild[node] in seen:
                    return False
                seen.add(rightChild[node])
                stack.append(rightChild[node])
        
        return len(seen) == n