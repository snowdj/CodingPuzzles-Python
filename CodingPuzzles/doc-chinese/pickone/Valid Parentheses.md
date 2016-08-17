# Problem

http://www.lintcode.com/en/problem/valid-parentheses/?rand=true

Given a string containing just the characters ```'('```, ```')'```, ```'{'```, ```'}'```, ```'['``` and ```']'```, determine if the input string is valid.

**Example**

The brackets must close in the correct order, ```"()"``` and ```"()[]{}"``` are all valid but ```"(]"``` and ```"([)]"``` are not.

# Thoughts

- Use stack
- If character is [, (, {, push to stack
- If character is ], ), }, pop stack and check if the poped element is the matching pair

# My Solution

```
    def isValidParentheses(self, s):
        # Write your code here
        valid = False
        if s == None:
            return valid
        
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True
```

# Reference

http://www.cnblogs.com/zuoyuan/p/3779772.html