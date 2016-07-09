from CodingPuzzles.binarytree.lib import binarytree1

tree = binarytree1.BinaryTree1()
root = tree.getroot()

import sys

def maxDepth(root):
    if root is None:
        return 0

    return getMaxD(root)

def getMaxD(node):
    if node is None:
        return -sys.maxint-1

    if node.left is None and node.right is None:
        return 1

    maxD = max(getMaxD(node.left), getMaxD(node.right)) + 1

    return maxD

def main():
    d = maxDepth(root)
    print "max depth: ", d

    if d == tree.get_maxd():
        print "Max Depth is correct!"
    else:
        print "Max Depth is wrong!"

if __name__ == '__main__':
    main()