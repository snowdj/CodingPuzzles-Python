# Problem

http://www.lintcode.com/en/problem/top-k-largest-numbers-ii/

Implement a data structure, provide two interfaces:

- ```add(number)```. Add a new number in the data structure.
- ```topk()```. Return the top k largest numbers in this data structure. k is given when we create the data structure.

**Example**

```
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
```

# Thoughts

- Use heapq data structure in Python

# My Solution

```
import heapq

class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.heap = []
        self.k = k

        
    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        heapq.heappush(self.heap, num)


    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        return heapq.nlargest(self.k, iter(self.heap))
```

# Reference

