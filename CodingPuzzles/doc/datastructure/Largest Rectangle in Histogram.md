# Problem

http://www.lintcode.com/en/problem/largest-rectangle-in-histogram/

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Thoughts

- Use a stack to keep track of the height and start indexes. Compare the current height with previous one.
- Use another stack to keep track of the index of each starting position of possible rectangle
- Case 1: current > previous (top of height stack)
Push current height and index as candidate rectangle start position.
- Case 2: current = previous
Ignore.
- Case 3: current < previous
Need keep popping out previous heights, and compute the candidate rectangle with height and width (current index - previous index). Push the height and index to stacks.

# My Solution

```
def largestRectangleArea(height):
    maxArea = 0
    stackHeight = []
    stackIndex = []
    for i in range(len(height)):
        if stackHeight == [] or height[i] > stackHeight[len(stackHeight)-1]:
            stackHeight.append(height[i])
            stackIndex.append(i)
        elif height[i] < stackHeight[len(stackHeight)-1]:
            lastIndex = 0
            while stackHeight and height[i] < stackHeight[len(stackHeight)-1]:
                lastIndex = stackIndex.pop()
                tempArea = stackHeight.pop() * (i - lastIndex)
                if maxArea < tempArea:
                    maxArea = tempArea
                stackHeight.append(height[i])
                stackIndex.append(lastIndex)
    while stackHeight:
        tempArea = stackHeight.pop() * (len(height) - stackIndex.pop())
        if tempArea > maxArea:
            maxArea = tempArea
    
    return maxArea
            
        
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3783993.html