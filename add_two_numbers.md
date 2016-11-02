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