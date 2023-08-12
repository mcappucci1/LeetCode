class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def moveNodeToFront(self, node: Node) -> None:
        node.prev, node.next = self.head, self.head.next
        head_next = self.head.next
        self.head.next, head_next.prev = node, node

    def removeNode(self, key: int) -> Node:
        node = None
        if key in self.keys:
            node = self.keys[key]
            prev, nextt = node.prev, node.next
            nextt.prev, prev.next = prev, nextt
        return node

    def get(self, key: int) -> int:
        val = -1
        node = self.removeNode(key)
        if node:
            self.moveNodeToFront(node)
            val = node.val
        return val

    def put(self, key: int, value: int) -> None:
        node = self.removeNode(key)
        if node:
            self.moveNodeToFront(node)
            node.val = value
            return
        node = Node(key, value)
        self.keys[key] = node
        self.moveNodeToFront(node)
        if len(self.keys) > self.capacity:
            last_node = self.removeNode(self.tail.prev.key)
            del self.keys[last_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)