import os, sys

import binarynode

class BinaryTree0():
###############
#    4
#   / \
#  3   5
# / \   \
#0  2   -1
    def __init__(self):
        node0 = binarynode.BinaryNode(0)
        node1 = binarynode.BinaryNode(2)
        node2 = binarynode.BinaryNode(-1)
        node3 = binarynode.BinaryNode(3, node0, node1)
        node4 = binarynode.BinaryNode(5, None, node2)
        node5 = binarynode.BinaryNode(4, node3, node4)
        self.root = node5

    def getroot(self):
        return self.root
