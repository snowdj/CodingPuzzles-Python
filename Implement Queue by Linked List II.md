# Problem

Implement a Queue by linked list. Provide the following basic methods:

- ```push_front(item)```. Add a new item to the front of queue.
- ```push_back(item)```. Add a new item to the back of the queue.
- ```pop_front()```. Move the first item out of the queue, return it.
- ```pop_back()```. Move the last item out of the queue, return it.

**Example**

```
push_front(1)
push_back(2)
pop_back() // return 2
pop_back() // return 1
push_back(3)
push_back(4)
pop_front() // return 3
pop_front() // return 4
```

# Thoughts
- Use a linked list with a head pointer and a tail pointer
- In a deque, each node has two pointers: prev, next. Make sure updating the two pointers when manipulating nodes
- push front: put the element in the linked list as head (O(n))
- push back: put the element in the linked list as tail (O(1))
- pop_front: return the head of linked list, update new head (O(n))
- pop_back: return the tail of linked list (O(n))

# My Solution

```
class Dequeue(object):
    def __init__(self):
        self.first = None
        self.last = None
    
    def push_front(self, item):
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
        else:
            temp = self.first
            self.first = Node(item)
            self.first.next = temp
            temp.prev = self.first
    
    def push_back(self, item):
        if self.last is None:
            self.first = Node(item)
            self.last = self.first
        else:
            tmp = Node(item)
            self.last.next = tmp
            tmp.prev = self.last
            self.last = tmp
    
    def pop_front(self):
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next
            if self.first is not None:
                self.first.prev = None
            else:
                self.last = None
            return item
        
        return None
    
    def pop_back(self):
        if self.last is not None:
            item = self.last.val
            self.last = self.last.prev
            if self.last is not None:
                self.last.next = None
            else:
                self.first = None
            return item
        
        return None

class Node():
    def __init__(self, _val):
        self.next = self.prev = None
        self.val = _val

```

# Reference

