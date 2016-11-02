# Problem

http://www.lintcode.com/en/problem/sort-letters-by-case/

Given a string which contains only letters. Sort it by lower case first and upper case second.

*Notice*
It's NOT necessary to keep the original order of lower-case letters and upper-case letters.

**Example**

For ```"abAcD"```, a reasonable answer is ```"acbAD"```. 

# Thoughts

- This problem is almost the same as the "Sort Color" problem
- Use two pointers pointing to the start and end of the chars
- If chars[start] is uppercase, and chars[end] is lowercase, swap the two chars
- Tips
  - Create functions isLower, isUpper to check the conditions
- Another method is using Python's library sort

# My Solution

## Solution 1: Using two pointers

```
    def sortLetters(chars):
        # write your code here
        if len(chars) == 0:
            return chars
        
        start = 0
        end = len(chars) - 1
        while start < end:
            if chars[start] >= 'A' and chars[start] <= 'Z' and chars[end] >= 'a' and chars[end] <= 'z':
                t = chars[end]
                chars[end] = chars[start]
                chars[start] = t
                start += 1
                end -= 1
            elif chars[start] >= 'A' and chars[start] <= 'Z':
                end -= 1
            else:
                start += 1
        
        return chars
```


```
    def sortLetters(chars):
        # write your code here
        if len(chars) == 0:
            return chars
        
        start = 0
        end = len(chars) - 1
        while start < end:
            while start < end and not chars[start].isupper():
                start += 1
            while start < end and chars[end].isupper():
                end -= 1
            if (start < end):
                t = chars[end]
                chars[end] = chars[start]
                chars[start] = t
        
        return chars
    
```

## Solution 2: Use Python's sort library

```
    def sortLetters(chars):
        chars.sort(key=lambda c: c.isupper())
```