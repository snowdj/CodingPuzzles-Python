import binary_tree
import balanced_binary_tree

# build a binary tree for testing
tTree = binary_tree.BinaryTree("3")
tTree.insertLeft("9")
tTree.insertRight("20")
tTree.insertLeft("15")
tTree.insertRight("7")

binary_tree.printTree(tTree)

