from CodingPuzzles.binarytree.lib import binarytree1

tree = binarytree1.BinaryTree1()
root = tree.getroot()

def serialize(root):
    # write your code here
    res = []

    if root is None:
        return res

    preorder(root, res)

    return res

def preorder(node, res):
    if node:
        res.append(node.item)
        preorder(node.left, res)
        preorder(node.right, res)
    else:
        res.append('#')

def serialize2(root):
    res = []

    if root is None:
        return res

    preorder2(root, res)

    return res

def preorder2(node, res):
    if node is None:
        return

    res.append(node.item)
    if node.left:
        preorder(node.left, res)
    else:
        res.append('#')
    if node.right:
        preorder(node.right, res)
    else:
        res.append('#')

def main():
    print(serialize(root))
    print(serialize2(root))

    if serialize(root) == serialize2(root):
        print("PASS")
    else:
        print("FAIL")



if __name__ == '__main__':
    main()