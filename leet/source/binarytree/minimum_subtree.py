class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = Node(5)
        node1_0 = Node(2)
        node1_1 = Node(3)
        node2_0 = Node(-1)
        node2_1 = Node(4)
        node2_2 = Node(2)
        node2_3 = Node(0)
        self.root.left = node1_0
        self.root.right = node1_1
        node1_0.left = node2_0
        node1_0.right = node2_1
        node1_1.left = node2_2
        node1_1.right = node2_3

        self.seq_preorder = []
        self.seq_inorder = []
        self.seq_postorder = []

    def preorder(self):
        self.preorder_helper(self.root)
        return self.seq_preorder

    def preorder_helper(self, node):
        if node is None:
            return
        self.seq_preorder.append(node.val)
        self.preorder_helper(node.left)
        self.preorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)
        return self.seq_inorder

    def inorder_helper(self, node):
        if node is None:
            return
        self.inorder_helper(node.left)
        self.seq_inorder.append(node.val)
        self.inorder_helper(node.right)

    def postorder(self):
        self.postorder_helper(self.root)
        return self.postorder

    def postorder_helper(self, node):
        if node is None:
            return
        self.postorder_helper(node.left)
        self.postorder_helper(node.right)
        self.seq_postorder.append(node.val)


class Solution():

    def findSubtree(self, root):
        # write your code here
        import sys
        self.min_sum = sys.maxint
        self.result = None

        self.search(root)
        return self.result

    def search(self, node):
        if node is None:
            return 0

        left_sum = self.search(node.left)
        right_sum = self.search(node.right)

        curr_sum = left_sum + right_sum + node.val
        if curr_sum <= self.min_sum:
            self.min_sum = curr_sum
            self.result = node

        return curr_sum

if __name__ == "__main__":
    tree = BinaryTree();
    result = tree.preorder()
    print(result)

    solution = Solution();
    result = solution.findSubtree(tree.root)
    print(result)


