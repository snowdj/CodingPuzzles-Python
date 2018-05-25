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
        # write your code here
        if root is None:
            return True

        self.last_val = None
        return self.validate(root)

    def validate(self, node):
        if node is None:
            return True

        is_bst = self.validate(node.left)
        if not is_bst:
            return False
        if self.last_val is not None and self.last_val >= node.val:
            return False

        self.last_val = node.val
        return self.validate(node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    sln = Solution()
    result = sln.isValidBST(tree.root)
    print(result)
