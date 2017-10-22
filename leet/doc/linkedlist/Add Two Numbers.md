# Problem

http://www.lintcode.com/en/problem/add-two-numbers/

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in *reverse* order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

**Example**

Given ```7->1->6 + 5->9->2```. That is, ```617 + 295```.

Return ```2->1->9```. that is ```912```.

Given ```3->1->5``` and ```5->9->2```, return ```8->0->8```.

# Thoughts

## Method 1
- Add the value of nodes in both two lists. As the digits are stored in the lists in  reverse order, no need to reorder the list.
- carry = (carry + val1 + val2 ) / 10
- sum = (carry + val1 + val2) % 10

Pay attention to:
* Create a dummy node as the head, then you don't need operate p.next = next node every time.
* Consider the length difference of two lists.
* The final result: consider two cases - carry == 1 (need create a node Node(1) as then end), carry == 0.

## Method 2
- Record the values of linked list nodes, and change to number (remember the reverse order)
- Sum the two numbers
- Change the result number to a linked list

# My Solution

```
    def addTwoNumbers(l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0); p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1 = l1.next; l2 = l2.next; p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next; p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next; p = p.next
        if flag == 1: p.next = ListNode(1)
        return dummy.next
```

## Python 3

```
class Node:
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next=None):
        self._next = next

# 123 + 456 = 579
# result: 9->7->5

a0 = Node(3)
a1 = Node(2)
a2 = Node(1)
a0.next = a1
a1.next = a2

b0 = Node(6)
b1 = Node(5)
b2 = Node(4)
b0.next = b1
b1.next = b2

def add_two_numbers(l0, l1):
    if l0 == None: return l1
    if l1 == None: return l0
    carry = 0
    dummy = Node(0)
    p = dummy
    
    while l0 and l1:
        p.next = Node((l0.value + l1.value + carry) % 10)
        carry = (l0.value + l1.value + carry) // 10
        l0 = l0.next
        l1 = l1.next
        p = p.next
    if l0:
        while l0:
            p.next = Node((l0.value + carry) % 10)
            carry = (l0.value + carry) // 10
            l0 = l0.next
            p = p.next
    if l1:
        while l1:
            p.next = Node((l1.value + carry) % 10)
            carry = (l1.value + carry) // 10
            l1 = l1.next
            p = p.next
    if carry == 1:
        p.next = Node(1)
    return dummy.next

result = Node(0)
result = add_two_numbers(a0, b0)
while (result):
    print(result.value)
    result = result.next
```