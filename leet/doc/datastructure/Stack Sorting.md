# Problem

http://www.lintcode.com/en/problem/stack-sorting/

Sort a stack in ascending order (with biggest terms on top).

You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (e.g. array).

**Example**

Given stack = 

```
| |
|3|
|1|
|2|
|4|
 -
```

return:

```
| |
|4|
|3|
|2|
|1|
 -
```

# Thoughts

- Use a helper stack
- 从origin stack中不断pop() element
对于helper stack，如果helper stack peek() < element，则将helper stack中的元素全部转移到origin stack
再将element push()到helper stack中
不断重复上述步骤，直到origin stack isEmpty
最后，所有的元素已经按照descending order排序好（smallest on top），只需将其转移到origin stack，则origin stack即为所需排序

# My Solution

```
#Your can use Stack class in your solution.
#class Stack:
#  def __init__(self, stk=[])
#    # use stk to initialize the stack
#  def isEmpty(self)
#    # return true is stack is empty or false/
#  def push(self, item)
#    # push a element into stack and return nothing
#  def pop(self)
#    # pop a element from stack
#  def peek(self):
#    # return the top element if stack is not empty or nothing
#  def size(self):
#    # return the size of stack

def stackSorting(self, stk):
    tmp = Stack()
    while not stk.isEmpty():
        if not stk.isEmpty() and (tmp.isEmpty() or tmp.peek() >= stk.peek()):
            tmp.push(stk.peek())
            stk.pop()
        else:
            value = stk.peek()
            stk.pop()
            while not tmp.isEmpty() and tmp.peek() <= value:
                stk.push(tmp.peek())
                tmp.pop()
            
            stk.push(value)
            while not tmp.isEmpty():
                stk.push(tmp.peek())
                tmp.pop()
    
    while not tmp.isEmpty():
        stk.push(tmp.peek())
        tmp.pop()
```

# Reference

