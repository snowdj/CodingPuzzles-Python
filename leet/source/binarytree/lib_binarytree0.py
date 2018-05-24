import os, sys

from binarynode import BinaryNode

class BinaryTree0():
###############
#    4
#   / \
#  3   5
# / \   \
#0  2   -1

    def __init__(self):
        node0 = BinaryNode(0)
        node1 = BinaryNode(2)
        node2 = BinaryNode(-1)
        node3 = BinaryNode(3, node0, node1)
        node4 = BinaryNode(5, None, node2)
        node5 = BinaryNode(4, node3, node4)
        self.root = node5
        self.node0 = node0
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4

    def getroot(self):
        return self.root

    def getnode0(self):
        return self.node0

    def getnode4(self):
        return self.node4
