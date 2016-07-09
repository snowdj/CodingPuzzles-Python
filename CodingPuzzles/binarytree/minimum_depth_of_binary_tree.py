from CodingPuzzles.binarytree.lib import binarytree1

tree = binarytree1.BinaryTree1()
root = tree.getroot()

import sys

def minDepth(root):
    if root is None:
        return 0

    return getMinD(root)

def getMinD(node):
    if node is None:
        return sys.maxint

    if node.left is None and node.right is None:
        return 1

    minD = min(getMinD(node.left), getMinD(node.right)) + 1

    return minD

def main():
    d = minDepth(root)
    print "min depth: ", d

    if d == tree.get_mind():
        print "Min Depth is correct!"
    else:
        print "Min Depth is wrong!"

if __name__ == '__main__':
    main()