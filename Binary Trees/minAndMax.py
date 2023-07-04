from queue import Queue


class BTnode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


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

def minAndMax(root):
    if root is None:
        return 9999,-1
    lmin,lmax=minAndMax(root.left)
    rmin,rmax=minAndMax(root.right)
    
    return min(root.data,min(lmin,rmin)),max(root.data,max(lmax,rmax))
    



root = treeInput()
printLevelwise(root)
print(minAndMax(root))

