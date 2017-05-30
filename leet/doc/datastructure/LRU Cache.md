# Problem

http://www.lintcode.com/en/problem/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: ```get``` and ```set```.

```get(key)``` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
```set(key, value)``` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Thoughts

- Use hash to reach O(1) when looking up in the cache
- Use a double headed linked list (head, tail, with two pointers, next, prev)
- The data structure is: Linked Hash Map
- When looking up an element not in the cache, add this element to the head of the linked list
- The element in the end of the linked list is the least recently used one, and can be removed from cache when cache capacity is reached
- Note the head and tails are only markers, they are not used to process the cache values

# My Solution

```
# Definition for a doubly-linked list node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dummyNode = Node(-1, -1)
        self.tail = self.dummyNode
        self.entryFinder = {}

    # @return an integer
    def get(self, key):
        entry = self.entryFinder.get(key)
        if entry is None:
            return -1
        else:
            self.renew(entry)
            return entry.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        entry = self.entryFinder.get(key)
        if entry is None:
            entry = Node(key, value)
            self.entryFinder[key] = entry
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
            if self.size < self.capacity:
                self.size += 1
            else:
                headNode = self.dummyNode.next
                if headNode is not None:
                    self.dummyNode.next = headNode.next
                    headNode.next.prev = self.dummyNode
                del self.entryFinder[headNode.key]
        else:
            entry.val = value
            self.renew(entry)
    
    def renew(self, entry):
        if self.tail != entry:
            prevNode = entry.prev
            nextNode = entry.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            entry.next = None
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
```

# Reference 

- http://bookshadow.com/weblog/2015/01/08/leetcode-lru-cache/





