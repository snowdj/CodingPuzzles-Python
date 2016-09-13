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

