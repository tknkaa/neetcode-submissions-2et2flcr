class LRUCache:
    def __init__(self, capacity: int):
        self.map: Dict[int, Node] = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            target = self.map[key]
            target.prev.next = target.next
            target.next.prev = target.prev

            target.prev = self.tail.prev
            target.next = self.tail

            self.tail.prev.next = target
            self.tail.prev = target

            return target.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            target = self.map[key]
            target.prev.next = target.next
            target.next.prev = target.prev
            target.val = value

            target.prev = self.tail.prev
            target.next = self.tail

            self.tail.prev.next = target
            self.tail.prev = target
        elif len(self.map) == self.capacity:
            del self.map[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

            node = Node(key, value)
            node.prev = self.tail.prev
            node.next = self.tail

            self.tail.prev.next = node
            self.tail.prev = node

            self.map[key] = node
        else:
            node = Node(key, value)
            node.prev = self.tail.prev
            node.next = self.tail

            self.tail.prev.next = node
            self.tail.prev = node

            self.map[key] = node

class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next