class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev
    
    def remove(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return
        
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_front(self, node):
        if node == self.head:
            return
        self.remove(node)
        self.add_to_front(node)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lst = DoublyLinkedList()
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.lst.move_to_front(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.cache:
            self.lst.remove(self.cache[key])
            self.lst.add_to_front(new_node)
            self.cache[key] = new_node
            return

        if len(self.cache) >= self.capacity:
            lru = self.lst.tail
            self.lst.remove(lru)
            del self.cache[lru.key]

        self.cache[key] = new_node
        self.lst.add_to_front(new_node)