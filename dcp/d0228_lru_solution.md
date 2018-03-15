To implement both these methods in constant time, we'll need to use a hash table along with a linked list. The hash table will map keys to nodes in the linked list, and the linked list will be ordered from least recently used to most recently used. Then, for set:

First look at our current capacity. If it's < n, then create a node with the val, set it as the head, and add it as an entry in the dictionary.
If it's equal to n, then add our node as usual, but also evict the least frequently used node by deleting the tail of our linked list and also removing the entry from our dictionary. We'll need to keep track of the key in each node so that we know which entry to evict.
For get:

If the key doesn't exist in our dictionary, then return null.
Otherwise, look up the relevant node through the dictionary. Before returning it, update the linked list by moving the node to the front of the list.
To help us out, we can use the following tricks:

- Using dummy nodes for the head and tail of our list, which will simplify creating the list when nothing's initialized.
- Implementing the helper class LinkedList to reuse code when adding and removing nodes to our linked list.
- When we need to bump a node to the back of list (like when we fetch it), we can just remove it and readd it.

Euccas Notes:

The hash table and linkedlist doesn't have connection. This is not like the zlib hash chain organization, which has a chain for each position in the hash table. Here in this case, the linkedlist is for all elements in the cache, and there is only ONE linked list.

In the example solution, the linked list is a double ended linked list (has a prev pointer, and a next pointer). Is it possible to use a single end linked list?
- No. Because to keep add() operation O(1), we don't want to iterate over the whole linked list to find the tail. We need use prev pointer to get the tail (before the dummy tail).

This kind of problem focuses on *data structure*. For such problems, try to think about OO design, which usually could make coding easier and cleaner.

