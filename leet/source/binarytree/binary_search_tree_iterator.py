from lib_binary_tree import BinaryTree

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""

class BSTIterator():
    def __init__(self, root):
        self.stack = []
        self.curr = root

    # return: True if there has next node, or false
    def hasNext(self):
        return self.curr is not None or len(self.stack) > 0

    # return: next node
    def next(self):
        while self.curr is not None:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        next = self.curr
        self.curr = self.curr.right
        return next

if __name__ == "__main__":
    tree = BinaryTree()
    iter = BSTIterator(tree.root)
    while iter.hasNext():
        node = iter.next()
