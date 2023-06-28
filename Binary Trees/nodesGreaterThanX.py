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


def bigNodes(root,x):
    if root == None:
        return 0
    count=0
    if root.data > x:
        count+=1
    leftLargest = bigNodes(root.left, x)
    rightLargest = bigNodes(root.right, x)
    return leftLargest + rightLargest + count


root = treeInput()
printTreeDetailed(root)
print(bigNodes(root,1))
