# Problem

http://www.lintcode.com/en/problem/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

**Example**

Given lists:

```
[
  2->4->null,
  null,
  -1->null
],
```

return ```-1 -> 2 -> 4 -> null```

# Thoughts

- Use data structure heap
- Push the head of every list in the heap
- Pop the head of the heap (the smallest element)
- Then find the next element of the poped element from the original list, and push it to the heap
- Heap methods
    - heapq.heapify(list)
    - heapq.heappush(list, item)
    - heapq.heappop(list)

# My Solution

```
def mergeKLists(lists):
    heap = []
    for node in lists:
        if node:
            heap.append((node.val, node))
    heapq.heapify(heap)
    head = ListNode(0)
    curr = head
    while heap:
        pop = heapq.heappop(heap)
        curr.next = ListNode(pop[0])
        curr = curr.next
        if pop[1].next:
            heapq.heappush(heap, (pop[1].next.val, pop[1].next))
            
     return head.next
```

# Reference

- https://docs.python.org/2/library/heapq.html

