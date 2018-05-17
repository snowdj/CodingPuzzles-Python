# Method: traverse
def find_max_depth_by_traverse(root):
    if root is None:
        return 0

    depth = 0
    dfs(root, 1)
    return depth

def dfs(node, curr_depth):
    if node is None:
        return

    depth = 