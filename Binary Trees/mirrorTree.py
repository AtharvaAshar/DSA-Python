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


def mirrorTree(root):
    if root is None:
        return
    mirrorTree(root.left)
    mirrorTree(root.right)
    root.left,root.right=root.right,root.left 
    return root


root = treeInput()
printTreeDetailed(root)
root_new=mirrorTree(root)
printTreeDetailed(root_new)
