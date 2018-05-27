"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution_bruteforce:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if root is None or target is None:
            return None

        self.inorder_seq = []
        self.inorder_traverse(root)

        self.result = self.inorder_seq
        self.findK(target, k)

        return self.result

    def inorder_traverse(self, node):
        if node is None:
            return

        self.inorder_traverse(node.left)
        self.inorder_seq.append(node.val)
        self.inorder_traverse(node.right)

    def findK(self, target, k):
        while len(self.result) > k:
            if target - self.result[0] > self.result[-1] - target:
                self.result.pop(0)
            else:
                self.result.pop(-1)

