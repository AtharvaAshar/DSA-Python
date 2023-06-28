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


def printNodeAtK(root,k):
    if root is None:
        return
    if k==0:
        print("Node : ",root.data)
        return
    leftTree=printNodeAtK(root.left,k-1)
    rightTree=printNodeAtK(root.right,k-1)


def printNodeAtKPart2(root, k,d=0):
    if root is None:
        return
    if k == d:
        print(f"Node at depth {d}: {root.data} ")
        return
    leftTree = printNodeAtKPart2(root.left, k,d+1)
    rightTree = printNodeAtKPart2(root.right, k,d+1)

root = treeInput()
printTreeDetailed(root)
printNodeAtK(root,2)
printNodeAtKPart2(root,2)

