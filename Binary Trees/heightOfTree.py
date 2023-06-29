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


def height(root):
    if root == None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return max(leftHeight,rightHeight) + 1

def isBalanced(root):
    if root == None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh > 1 or rh-lh > 1:
        return False
    isLeftBalanced=isBalanced(root.left)
    isRightBalanced=isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else: return False


root = treeInput()
printTreeDetailed(root)
print(isBalanced(root))
