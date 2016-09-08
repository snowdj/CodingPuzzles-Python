# Problem

http://www.lintcode.com/en/problem/implement-queue-by-two-stacks/

As the title described, you should only use two stacks to implement a queue's actions.

The queue should support ```push(element)```, ```pop()``` and ```top()``` where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

**Example**

```
push(1)
pop()   // return 1
push(2)
push(3)
top()   // return 2
pop()   // return 2
```

# Thoughts

- A queue has three operations: push, pop, top
- push: put elements to stack 1
- top: adjust from stack 1 to stack 2, then return the last element (top, -1) in stack 2, which was the first element in stack 1
- pop: adjust from stack 1 to stack 2, then pop stack 2 to remove the element which was the first element in stack 1
- adjust: pop from stack 1 and push to stack 2; only do this when stack 2 is empty. When stack 2 is not empty, pop and top result will not be affected by the new elements in stack 1
- Note when implementing with Python, stacks are actually list data structure. list.pop returns the first element in the list. list[-1] is the last element of the list.

# My Solution

```
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
   
   def push(self, element):
        self.stack1.append(element)
   
   def top(self):
        self.adjust()
        return self.stack2[-1]
   
   def pop(self):
        self.adjust()
        return self.stack2.pop()
```


