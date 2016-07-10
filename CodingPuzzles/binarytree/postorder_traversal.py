from CodingPuzzles.binarytree.lib import binarytree1

tree = binarytree1.BinaryTree1()
root = tree.getroot()

def postorder(root, result):
    if root is None:
        return

    if root.left:
        postorder(root.left, result)

    if root.right:
        postorder(root.right, result)

    result.append(root.item)

def main():
    result = []
    postorder(root, result)
    print "post order traversal result: ", result

    if result == tree.get_postorder():
        print "PASS"
    else:
        print "FAIL"

if __name__ == '__main__':
    main()