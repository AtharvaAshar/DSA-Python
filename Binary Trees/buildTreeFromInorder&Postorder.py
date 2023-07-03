from queue import Queue


class BTnode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    if len(postorder) == 0:
        return None
    root = postorder[-1]
    root = BTnode(root)
    i = inorder.find(root.data)
    leftInorder = inorder[:i]
    rightInorder = inorder[i+1:]
    leftPostorder = postorder[:len(leftInorder)]
    rightPostorder = postorder[len(leftInorder):-1]
    leftSubTree = buildTree(leftInorder, leftPostorder)
    rightSubTree = buildTree(rightInorder, rightPostorder)
    root.left = leftSubTree
    root.right = rightSubTree
    return root


def printLevelwise(root):
    q = Queue()
    q.put(root)
    while not (q.empty()):
        curr = q.get()
        print(curr.data, end=":")
        if curr.left is not None:
            print("L", curr.left.data, end=",")
            q.put(curr.left)
        if curr.right is not None:
            print("R", curr.right.data, end=" ")
            q.put(curr.right)
        print()


postorder = "4526731"
inorder = "4251637"
root = buildTree(inorder, postorder)
printLevelwise(root)
