class Solution():
    def kthSmallest(self, root, k):
        # write your code here
        if root is None:
            return None

        self.seq = []
        self.inorder(root, k)
        if len(self.seq) >= k:
            return self.seq[k-1]
        return None

    def inorder(self, node, k):
        if node is None:
            return

        self.inorder(node.left, k)
        self.seq.append(node.val)
        if len(self.seq) >= k:
            return
        self.inorder(node.right, k)

class Solution1():
    def kthSmallest(self, root, k):
        self.result = root.val
        self.count = 0
        self.traverse(root, k)
        return self.result

    def traverse(self, root, k):
        if root is None or self.count >= k:
            return

        self.traverse(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val

        self.traverse(root.right, k)