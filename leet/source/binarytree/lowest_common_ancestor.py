from lib_binarytree0 import BinaryTree0

tree = BinaryTree0()
root = tree.getroot()
node0 = tree.getnode0()
node4 = tree.getnode4()

def lca(node, nodeA, nodeB):
    if node is None:
        print("node is None")
    else:
        print("node is ", node.item)
        if node == nodeA or node == nodeB:
            print("node is the given target")

    if (node is None or node == nodeA or node == nodeB):
        return node

    print("-- node ", node.item, "try left")
    left = lca(node.left, nodeA, nodeB)
    if left is None:
        print("-- node", node.item, "left: None")
    else:
        print("-- node ", node.item, "left: ", left.item)


    print("-- node ", node.item, "try right")
    right = lca(node.right, nodeA, nodeB)
    if right is None:
        print("-- node ", node.item, "right: None")
    else:
        print("-- node ", node.item, "right: ", right.item)

    if (left and right):
        print("** node ", node.item, "left and right")
        return node
    if left is None:
        print("** node ", node.item, "left is None")
        return right
    if right is None:
        print("** node ", node.item, "right is None")
        return left

    return None

def main():
    anode = lca(root, node0, node4)

    print("result: ")
    print(anode.item)

if __name__ == '__main__':
    main()