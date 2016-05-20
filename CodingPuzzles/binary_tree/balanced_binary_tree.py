def isBalanced(root):
    balanced, height = validate(root)
    return balanced

def validate(root):
    if root is None:
        return True, 0

    balanced, leftHeight = validate(root.left)
    if not balanced:
        return False, 0

    balanced, rightHeight = validate(root.right)
    if not balanced:
        return False, 0

    return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1