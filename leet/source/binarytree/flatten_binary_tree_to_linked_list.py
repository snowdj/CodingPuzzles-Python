from lib_binary_tree import Node
from lib_binary_tree import BinaryTree

class Solution_traverse():
    def flatten(self, root):
       if root is None:
           return None

       self.lastNode = None
       self.dfs(root)
       return root

    def dfs(self, node):
        if node is None:
            return

        if self.lastNode is not None:
            self.lastNode.left = None
            self.lastNode.right = node

        self.lastNode = node
        right = node.right
        self.dfs(node.left)
        self.dfs(right)

class Solution_dc():
    def flatten(self, root):
        if root is None:
            return None

        self.dfs(root)
        return root

    def dfs(self, node):
        if node is None:
            return None

        leftLast = self.dfs(node.left)
        rightLast = self.dfs(node.right)
        if leftLast is not None:
            leftLast.right = node.right
            node.right = node.left
            node.left = None

        if rightLast is not None:
            return rightLast

        if leftLast is not None:
            return leftLast

        return node

if __name__ == "__main__":
    tree = BinaryTree();
    print(tree.preorder())

    sln = Solution_traverse()
    sln.flatten(tree.root)

    tree = BinaryTree();
    print(tree.preorder())

    sln = Solution_dc()
    sln.flatten(tree.root)


