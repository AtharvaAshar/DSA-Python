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


def replaceWithDepth(root,k=0):
    if root is None:
        return
    root.data=k
    leftTree = replaceWithDepth(root.left, k+1)
    rightTree=replaceWithDepth(root.right,k+1)


root = treeInput()
printTreeDetailed(root)
replaceWithDepth(root)
printTreeDetailed(root)