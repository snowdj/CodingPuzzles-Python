__all__ = ['Node', 'BinaryTree']

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = Node(5)
        self.node1_0 = Node(2)
        self.node1_1 = Node(3)
        self.node2_0 = Node(-1)
        self.node2_1 = Node(4)
        self.node2_2 = Node(2)
        self.node2_3 = Node(0)
        self.root.left = self.node1_0
        self.root.right = self.node1_1
        self.node1_0.left = self.node2_0
        self.node1_0.right = self.node2_1
        self.node1_1.left = self.node2_2
        self.node1_1.right = self.node2_3

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

if __name__ == "__main__":
    tree = BinaryTree();
    result = tree.preorder()
    print(result)