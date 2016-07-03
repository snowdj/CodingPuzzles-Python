import os, sys

import binarynode
import binarytree0

tree = binarytree0.BinaryTree0()
root = tree.getroot()

def levelorder(node, level, result):
    print "level = %s" % level;

    if node:
        if len(result) < level + 1:
            result.append([])

        print "-- append node ", node.item, "to level ", level
        result[level].append(node.item)

        levelorder(node.left, level+1, result)
        levelorder(node.right, level+1, result)

def main():
    result = []
    levelorder(root, 0, result)

    print "result: "
    idx = 0
    for levels in result:
        print "level: %d" % idx
        idx += 1
        for node in levels:
            print node

if __name__ == '__main__':
    main()