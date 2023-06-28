class BTnode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def treeInput():
    nodeData = int(input("Enter node data : "))
    if nodeData == -1:
        return None
    node = BTnode(nodeData)
    leftTree = treeInput()
    rightTree = treeInput()
    node.left = leftTree
    node.right = rightTree
    return node

def countLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    leafLeft=countLeaf(root.left)
    leafRight=countLeaf(root.right)
    return leafLeft + leafRight

root = treeInput()
printTreeDetailed(root)
print(countLeaf(root))

