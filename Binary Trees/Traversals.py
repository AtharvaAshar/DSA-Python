class BTnode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()

def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.data,end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    inOrderTraversal(root.right)



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





root = treeInput()
print("Pre order Traversal")
preOrderTraversal(root)
print("Post order Traversal")
postOrderTraversal(root)
print("InOrder Traversal")
inOrderTraversal(root)

