# Problem

http://www.lintcode.com/en/problem/implement-stack/

Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

**Example**

```
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
```

# Thoughts

- In Python, use list to implement the stack
- push: append to the list
- pop: list.pop() - default is popping the last element
- top: return list[-1]
- isEmpty: len(list) == 0?

# My Solution

```
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        self.data.pop(-1)
    
    def top(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []
    
```


