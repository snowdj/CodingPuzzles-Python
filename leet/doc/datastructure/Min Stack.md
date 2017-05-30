# Problem

http://www.lintcode.com/en/problem/min-stack/

Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

*Notice*

min operation will never be called if there is no number in the stack.

**Example**

```
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1
```

# Thoughts

- To get the min value at any time, maintain a min stack, update the min stack when pusing and poping
- One thing need notice is when do you need remove the element from min stack when poping the stack

# My Solution

```
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []
   
    def push(self, number):
        self.stack.append(number)
        if len(self.minstack == 0) or number <= self.minstack[-1]:
            self.minstack.append(number)
    
    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()
    
    def min(self):
        return self.minstack[-1]
```