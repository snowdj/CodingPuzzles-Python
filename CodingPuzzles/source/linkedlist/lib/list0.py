import os, sys

from CodingPuzzles.linkedlist.lib import listnode

class LinkedList0:
    # 9 -> 2 -> 8 -> 8
    def __init__(self):
        node0 = listnode.ListNode(9)
        node1 = listnode.ListNode(2)
        node2 = listnode.ListNode(8)
        node3 = listnode.ListNode(8)

        node0.next = node1
        node1.next = node2
        node2.next = node3

        self.head = node0
        self.tail = node3

        return node0

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def getLen(self):
        return 4