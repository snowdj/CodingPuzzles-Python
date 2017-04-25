from CodingPuzzles.binarytree.lib import binarytree1

tree = binarytree1.BinaryTree1()
root = tree.getroot()

def inorder(root, result):
    if root is None:
        return

    if root.left:
        inorder(root.left, result)

    result.append(root.item)

    if root.right:
        inorder(root.right, result)

def main():
    result = []
    inorder(root, result)
    print "in order traversal result: ", result

    if result == tree.get_inorder():
        print "PASS"
    else:
        print "FAIL"

if __name__ == '__main__':
    main()