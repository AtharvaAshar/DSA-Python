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

root = treeInput()
levelOrderTraversal(root)
