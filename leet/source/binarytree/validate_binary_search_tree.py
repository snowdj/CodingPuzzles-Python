class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = Node(10)
        self.node1_0 = Node(5)
        self.node1_1 = Node(15)
        self.node2_2 = Node(6)
        self.node2_3 = Node(20)
        self.root.left = self.node1_0
        self.root.right = self.node1_1
        self.node1_1.left = self.node2_2
        self.node1_1.right = self.node2_3

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True

        self.validate(root)

        return self.isBST

    def validate(self, root):
        if root is None:
            return

        self.validate(self.left)
        if self.lastVal is not None and self.lastVal > root.val:
            self.isBST = False
            return

        self.lastVal = root.val
        self.validate(root.right)

