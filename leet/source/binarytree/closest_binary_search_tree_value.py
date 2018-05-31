# O(n), n is the number of nodes in the binary tree
class Solution():
    def closestValue(self, root, target):
        # write your code here
        if root is None or target is None:
            return None

        import sys
        self.min_diff = sys.maxint
        self.result = None
        self.search(root, target)
        return self.result.val

    def search(self, node, target):
        if node is None:
            return

        curr_diff = abs(node.val - target)
        if curr_diff < self.min_diff:
            self.min_diff = curr_diff
            self.result = node

        self.search(node.left, target)
        self.search(node.right, target)

# O(h), h is the height of the binary tree
class Solution1():
    def cloestValue(self, root, target):
        if root is None or target is None:
            return None

        lowerNode = self.lowerBound(root, target)
        upperNode = self.upperBound(root, target)

        if lowerNode is None:
            return upperNode.val
        if upperNode is None:
            return lowerNode.val
        if target - lowerNode.val > upperNode.val - target:
            return upperNode.val
        return lowerNode.val

    def lowerBound(self, node, target):
        if node is None:
            return None

        if target <= node.val:
            return self.lowerBound(node.left, target)

        lowerNode = self.lowerBound(node.right, target)
        if lowerNode is not None:
            return lowerNode

        return node

    def upperBound(self, node, target):
        if node is None:
            return None

        if target >= node.val:
            return self.upperBound(node.right, target)

        upperNode = self.upperBound(node.left, target)
        if upperNode is not None:
            return upperNode

        return node

"""
This method is easier to understand.
Similar to binary search.
"""
class Solution2(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None or target is None:
            return None

        self.result = root.val
        self.search(root, target)
        return self.result

    def search(self, node, target):
        if node is None:
            return

        if abs(target - self.result) > abs(target - node.val):
            self.result = node.val

        if target > node.val:
            self.search(node.right, target)
        else:
            self.search(node.left, target)
