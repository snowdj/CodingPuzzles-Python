from lib_binary_tree import Node
from lib_binary_tree import BinaryTree

class Solution():
    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, curr_path):
        curr_path.append(str(node.val))

        if node.left is None and node.right is None:
            result.append('->'.join(curr_path))
            curr_path.pop()
            return

        if node.left:
            self.dfs(node.left, result, curr_path)

        if node.right:
            self.dfs(node.right, result, curr_path)

        curr_path.pop()

if __name__ == "__main__":
    tree = BinaryTree();
    result = tree.preorder()
    print(result)

    sln = Solution();
    result = sln.binaryTreePaths(tree.root)
    print(result)