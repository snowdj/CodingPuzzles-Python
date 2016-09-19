# Problem

http://www.lintcode.com/en/problem/implement-stack-by-two-queues/

Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

**Example**

```
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
```

# Thoughts

- Use one queue
  - push(x): push to back
  - pop(): for all elements in queue except for the last one, pop from front then push to back. Then pop from front
  - top(): for all elements in queue, pop from front and push to back，use top to record the poped element, return top
  - empty(): check if queue is empty

# My Solution

## Solution 1: using one queue

```
class Stack:
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0)) # adjust in the queue, keep the order
        self.queue.pop(0)
    
    def top(self):
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
            
        return top
    
    def isEmpty(self):
        return self.queue == []
```

# Reference

- http://bookshadow.com/weblog/2015/06/11/leetcode-implement-stack-using-queues/
