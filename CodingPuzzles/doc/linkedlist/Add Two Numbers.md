# Problem

http://www.lintcode.com/en/problem/add-two-numbers/

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in *reverse* order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

**Example**

Given ```7->1->6 + 5->9->2```. That is, ```617 + 295```.

Return ```2->1->9```. that is ```912```.

Given ```3->1->5``` and ```5->9->2```, return ```8->0->8```.

# Thoughts

- Record the values of linked list nodes, and change to number (remember the reverse order)
- Sum the two numbers
- Change the result number to a linked list

# My Solution
