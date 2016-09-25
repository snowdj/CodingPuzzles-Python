# Problem

http://www.lintcode.com/en/problem/implement-queue-by-linked-list/

Implement a Queue by linked list. Support the following basic methods:

- ```enqueue(item)```. Put a new item in the queue.
- ```dequeue()```. Move the first item out of the queue, return it.

**Example**

```
enqueue(1)
enqueue(2)
enqueue(3)
dequeue() // return 1
enqueue(4)
dequeue() // return 2
```

# Thoughts

- Use a linked list with only a head pointer, or use a linked list with both a head and a tail pointer
- If using a linked list with a head pointer only, the solution will TLE (Time Limit Exceed) when the input is a large set
  - enqueue: O(1)
  - dequeue: O(n)
- Using a linked list with a head and a tail pointer have better performance
  - enqueue: O(1)
  - dequeue: O(1)

# My Solution

## Solution 1: Use a linked list with a head pointer

```
class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.first = None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        # Write yout code here
        if self.first is None:
            self.first = Node(item)
        else:
            tmp = self.first
            while tmp and tmp.next:
                tmp = tmp.next
            tmp.next = Node(item)

    # @return an integer
    def dequeue(self):
        # Write your code here
        if self.first is not None:
            tmp = self.first
            self.first = self.first.next
            return tmp.val
        else:
            return None

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None
```

## Solution 2: Use a linked list with a head pointer and a tail pointer

```
class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.first, self.last = None, None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        # Write yout code here
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    # @return an integer
    def dequeue(self):
        # Write your code here
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next
            return item

        return -1000

class Node():

    def __init__(self, _val):
        self.next = None
        self.val = _val
```


# Reference

