from CodingPuzzles.source.linkedlist.lib.listnode import ListNode

class LinkedList0:
    # 9 -> 2 -> 8 -> 8
    def __init__(self):
        node0 = ListNode(9)
        node1 = ListNode(2)
        node2 = ListNode(8)
        node3 = ListNode(8)

        node0.next = node1
        node1.next = node2
        node2.next = node3

        self.head = node0
        self.tail = node3

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def getLen(self):
        return 4