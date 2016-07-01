import os, sys

import binarynode
import binarytree0

tree = binarytree0.BinaryTree0()
root = tree.getroot()

def recursive_inorder(node, list):
    if node:
        print "Node: ", node.item
        print node.item, "-- Try left "
        recursive_inorder(node.left, list)
        list.append(node.item)
        print node.item, "-- Added to list: ", node.item
        print node.item, "-- Try right "
        recursive_inorder(node.right, list)
    else:
        print "Node is None"

def main():
    list = []
    recursive_inorder(root, list)

    print "result: "
    print list

if __name__ == '__main__':
    main()











