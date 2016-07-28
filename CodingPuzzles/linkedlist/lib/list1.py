import os, sys

from CodingPuzzles.linkedlist.lib import listnode

class LinkedList1:
    # 0 -> 2 -> 3 -> 1 -> 4
    def __init__(self):
        node0 = ListNode(0)
        node1 = ListNode(2)
        node2 = ListNode(3)
        node3 = ListNode(1)
        node4 = ListNode(4)
        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

        self.head = node0
        self.tail = node4

        return node0

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def getLen(self):
        return 5
