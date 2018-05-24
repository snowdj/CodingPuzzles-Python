from lib_binary_tree import Node, BinaryTree

class Solution():
    def lowestCommonAncestor(self, root, node1, node2):
        if root is None or root == node1 or root == node2:
            return root

        left = self.lowestCommonAncestor(root.left, node1, node2)
        right = self.lowestCommonAncestor(root.right, node1, node2)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left

        if right is not None:
            return right

        return None

if __name__ is "__main__":
    tree = BinaryTree()
    node_a = tree.node2_0
    node_b = tree.node2_3

    sln = Solution()
    result = sln.lowestCommonAncestor(tree.root, node_a, node_b)
    print(result)