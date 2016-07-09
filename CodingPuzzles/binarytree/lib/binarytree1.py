import os, sys

import binarynode

class BinaryTree1():
###############
#    1
#   / \
#  2   3
# /   / \
#4   5  6
#   /
#  7
################

    def __init__(self):
        node7 = binarynode.BinaryNode(7)
        node5 = binarynode.BinaryNode(5, node7, None)
        node6 = binarynode.BinaryNode(6)
        node3 = binarynode.BinaryNode(3, node5, node6)
        node4 = binarynode.BinaryNode(4)
        node2 = binarynode.BinaryNode(2, node4, None)
        node1 = binarynode.BinaryNode(1, node2, node3)

        self.root = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4
        self.node5 = node5
        self.node6 = node6
        self.node7 = node7

    def getroot(self):
        return self.root

    def getnode2(self):
        return self.node2

    def getnode3(self):
        return self.node3

    def get_mind(self):
        return 3

    def get_maxd(self):
        return 4