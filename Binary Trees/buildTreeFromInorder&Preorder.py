from queue import Queue
class BTnode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
def buildTree(inorder,preorder):
    if len(preorder)==0:return None
    root=preorder[0]
    root=BTnode(root)
    i=inorder.find(root.data)
    leftInorder=inorder[:i]
    rightInorder=inorder[i+1:]
    leftPreorder=preorder[1:len(leftInorder)+1]
    rightPreorder=preorder[1+len(leftInorder):]
    leftSubTree=buildTree(leftInorder,leftPreorder)
    rightSubTree=buildTree(rightInorder,rightPreorder)
    root.left=leftSubTree
    root.right=rightSubTree
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


preorder="1245367"
inorder="4251637"
root=buildTree(inorder,preorder)
printLevelwise(root)