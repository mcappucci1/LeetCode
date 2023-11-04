class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.count = None
        self.val = set()


class AllOne:

    def __init__(self):
        self.keys = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def inc(self, key: str) -> None:
        node = self.head if key not in self.keys else self.keys[key]
        count = 0 if node == self.head else node.count
        if node != self.head:
            node.val.remove(key)
        if node.next.count != count + 1:
            next_node = Node()
            next_node.count = count + 1
            next_node.next, next_node.prev = node.next, node
            node.next.prev, node.next = next_node, next_node
        node.next.val.add(key)
        self.keys[key] = node.next
        if (node != self.head) and (not node.val):
            node.prev.next, node.next.prev = node.next, node.prev

    def dec(self, key: str) -> None:
        node = self.keys[key]
        node.val.remove(key)
        if node.count != 1:
            if node.prev.count != node.count - 1:
                prev_node = Node()
                prev_node.count = node.count - 1
                prev_node.next, prev_node.prev = node, node.prev
                node.prev.next, node.prev = prev_node, prev_node
            node.prev.val.add(key)
            self.keys[key] = node.prev
        else:
            del self.keys[key]
        if not node.val:
            node.prev.next, node.next.prev = node.next, node.prev

    def getMaxKey(self) -> str:
        return '' if self.tail.prev == self.head else next(iter(self.tail.prev.val))

    def getMinKey(self) -> str:
        return '' if self.head.next == self.tail else next(iter(self.head.next.val))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()