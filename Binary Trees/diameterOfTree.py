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


def diameter(root):
    if root ==None: return 0,0
    lh,ld=diameter(root.left)
    rh,rd=diameter(root.right)
    h = 1 + max(lh, rh)
    return h,max(lh+rh,max(ld,rd))





root = treeInput()
# printTreeDetailed(root)
print(diameter(root))
