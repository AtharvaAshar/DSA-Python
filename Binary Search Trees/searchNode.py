from queue import Queue


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


def treeInput():
    q = Queue()
    rootData = int(input("Enter root node data "))
    if rootData == -1:
        return None
    root = BTnode(rootData)
    q.put(root)
    while not (q.empty()):
        curr = q.get()
        l = int(input(f"Enter left node of {curr.data} "))
        if l != -1:
            l = BTnode(l)
            curr.left = l
            q.put(l)
        r = int(input(f"Enter right node of {curr.data} "))
        if r != -1:
            r = BTnode(r)
            curr.right = r
            q.put(r)
    return root


def levelOrderTraversal(root):
    q = Queue()
    q.put(root)
    q.put(None)
    print()
    while not (q.empty()):
        curr = q.get()
        if curr is not None:
            print(curr.data, end=":")
            if curr.left is not None:
                print("L", curr.left.data, end=",")
                q.put(curr.left)
            if curr.right is not None:
                print("R", curr.right.data, end=" ")
                q.put(curr.right)
        else:
            if q.empty():
                break
            else:
                print()
                q.put(None)


def pathSum(root, k, s):
    if root == None:
        return
    if root.data <= k:
        s += str(root.data)
    if root.left is None and root.right is None:
        if root.data == k:
            print(f"Path equal to sum  is {s}")
            s = ""
        return
    pathSum(root.left, k-root.data, s)
    pathSum(root.right, k-root.data, s)


def printNodeAtK(root, k):
    if root is None:
        return
    if k == 0:
        print("Node : ", root.data)
        return
    leftTree = printNodeAtK(root.left, k-1)
    rightTree = printNodeAtK(root.right, k-1)


def search(root, x):
    if root is None: return None
    while root is  not None:
        if root.data==x: return True
        if x<root.data:
            root=root.left
        else: 
            root=root.right
    return False

root = treeInput()
target = int(input("Enter target: "))

levelOrderTraversal(root)
print()
print(search(root,target))



