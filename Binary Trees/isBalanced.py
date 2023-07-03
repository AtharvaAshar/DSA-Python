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
    nodeData = int(input())
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

def isBalanced2(root):
    if root == None:
        return 0,True # height =0 and isBalanced=True
    lh,isLeftBalanced=isBalanced2(root.left)
    rh,isRightBalanced=isBalanced2(root.right)
    h= 1 + max(lh,rh)
    if lh-rh > 1 or rh-lh > 1:
        return h,False
    if isLeftBalanced and isRightBalanced:
        return h,True
    else: return h,False


root = treeInput()
# printTreeDetailed(root)
print(isBalanced2(root))
