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

