class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None, "head")
        self.tail = Node(None, "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev

    def add(self, node):
        """add node to tail"""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        """remove node at any position"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class LRUCache:
    def __init__(self, n):
        self.n = n
        self.dict = {}
        self.list = LinkedList()

    def set(self, key, val):
        if key in self.dict:
            del self.dict[key]
        n = Node(key, val)
        self.list.add(n)
        self.dict[key] = n
        if len(self.dict) > self.n:
            head = self.list.get_head()
            self.list.remove(head) # Least Recent Used node
            if head.key in self.dict:
                del self.dict[head.key]

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]
            self.list.remove(n) # Remove first
            self.list.add(n) # Add to tail
            return n.val
