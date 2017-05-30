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

- Use one queue: push - O(1), pop - O(n), top - O(n)
  - push(x): Push to back
  - pop(): For all elements in queue except for the last one, pop from front then push to back. Then pop from front
  - top(): For all elements in queue, pop from front and push to back，use top to record the poped element, return top
  - empty(): Check if queue is empty

- Use two queues: push - O(n), pop - O(1), top - O(1)
  - push(x): Keep all the elements in queue1 in reverse order. In every push, put the new element in the empty queue2, and add elements in queue1 to queue2 (orders are reversed now). Swap queue1 and queue2, so now the first element in queue1 is the last one added to queue1.

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

## Solution 2: using two queues

```
class Stack:
    def __init__(self):
       self.q1 = []
       self.q2 = []
    
    def push(self, x):
        self.q2.append(x)
        while(len(self.q1) > 0):
            self.q2.append(self.q1.pop(0))
        
        tmp = self.q1
        self.q1 = self.q2
        self.q2 = tmp
    
    def pop(self):
        self.q1.pop(0)
    
    def top(self):
        return self.q1[0]
    
    def isEmpty(self):
        return len(self.q1) == 0
        
```

# Reference

- http://bookshadow.com/weblog/2015/06/11/leetcode-implement-stack-using-queues/
