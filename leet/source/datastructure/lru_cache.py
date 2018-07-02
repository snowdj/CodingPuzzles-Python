class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None, "head") # dummy head
        self.tail = Node(None, "tail") # dummy tail
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

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
        if node is None:
            return
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class LRUCache:
    def __init__(self, n):
        self.maxsize = n
        self.dict = {}
        self.list = LinkedList()

    def put(self, key, val):
        n = Node(key, val)
        if key in self.dict:
            exist_node = self.dict[key]
            self.dict[key] = n
            # swap node in list to end?
            self.list.remove(exist_node)
            self.list.add(n)
        else:
            if len(self.dict.keys()) >= self.maxsize:
                head = self.list.get_head()
                self.list.remove(head) # Least Recent Used node
                if head.key in self.dict:
                    del self.dict[head.key]
            self.dict[key] = n
            self.list.add(n)

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]
            self.list.remove(n) # Remove first
            self.list.add(n) # Add to tail
            return n.val
        return -1


# Your LRUCache object will be instantiated and called as such:
#obj = LRUCache(capacity)
#param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
# obj.put(2, 1)
# obj.put(1, 1)
# obj.put(2, 3)
# obj.put(4, 1)
# obj.get(1)
# obj.get(2)

obj.get(2)
obj.put(2, 6)
obj.get(1)
obj.put(1, 5)
obj.put(1, 2)
print(obj.get(1))
print(obj.get(2))
