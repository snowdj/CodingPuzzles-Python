# Problem

http://www.lintcode.com/en/problem/add-two-numbers-ii/

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in ```forward``` order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

Example:

Given ```6->1->7 + 2->9->5```. That is, ```617 + 295```.

Return ```9->1->2```. That is, ```912```.

# Thoughts

## Method 1 (my own):
1. Convert the two linked lists to two numbers need be added
2. Add the two numbers
3. Convert the sum to a list (use list comprehension)
4. Convert the list to a linked list. To make this process easier, use a dummy node as the head

This method has one problem, if the linked list is very long, the number can exceed the range of int/long.

## Method 2:
1. Reverse two linked lists
2. Use the method for "Add Two Numbers I" to solve it

# My Solution

## Method 1

```
def add_two_numbers(l0, l1):
    if l0 is None: return l1
    if l1 is None: return l0
    
    num0 = []
    num1 = []
    
    while (l0):
        num0.append(l0.value)
        l0 = l0.next
    while (l1):
        num1.append(l1.value)
        l1 = l1.next
    
    n0 = l2n(num0)
    n1 = l2n(num1)
    n_sum = n0 + n1
    n_list = [int(x) for x in str(n_sum)]
    
    # build up the result list
    dummy = Node(0)
    p = dummy
    for n in n_list:
        p.next = Node(n)
        p = p.next
    
    return dummy.next
    
def l2n(num_list):
    if num_list is None or len(num_list) == 0: return None
    num = 0
    for i, n in enumerate(num_list):
        num += n * pow(10, len(num_list)-i-1)
    return num

result = add_two_numbers(a0, b0)
while (result):
    print(result.value)
    result = result.next
```

## Method 2

