# Problem

http://www.lintcode.com/en/problem/merge-k-sorted-arrays/

Given *k* sorted integer arrays, merge them into one sorted array.

**Example**

Given 3 sorted arrays:

```
[
    [1,3,5,7],
    [2,4,6],
    [0,8,9,10,11]
]
```

return ```[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]```. 

# Thoughts

- One solution is using a Pythonist way

Why does this work: Since in any case, we have to traverse the whole every element in the list of arrays, the complexity is O (mn), where m is the length of the list and n is the average length of each array. Collections.sort() implements Timsort (see here, here and here) which on average has complexity O(nlogn). The time complexity is the same as using a priority queue, but with much shorter code.

- Another solution is using the heap data structure
    - Push the first element of each list to heap
    - Pop from the heap (gets the smallest value), push the next element of the poped element to heap
    - The smallest element poped from the heap can be added to the result list
    - As we need find the next element of the poped element, we need record which sub array the element belongs to (index), and the position in the sub list

# My Solution

## Solution 1

```
def mergekSortedArrays(arrays):
    if arrays is None or len(arrays) == 0:
        return None
    
    mergedArray = [j for array in arrays for j in array]
    return sorted(mergedArray)

```

## Solution 2

```
def mergekSortedArrays(arrays):
    result = []
    heap = []
    for index, array in enumerate(arrays):
        if len(array) == 0:
            continue
        heapq.heappush(heap, (array[0], index, 0))
    
    while len(heap):
        val, x, y = heap[0]
        heapq.heappop(heap)
        result.append(val)
        if y + 1 < len(arrays[x]):
            heapq.heappush(heap, (arrays[x][y+1], x, y+1))
    
    return result
```