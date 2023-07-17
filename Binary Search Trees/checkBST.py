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


def minAndMax(root):
    if root is None:
        return 9999, -1
    lmin, lmax = minAndMax(root.left)
    rmin, rmax = minAndMax(root.right)

    return min(root.data, min(lmin, rmin)), max(root.data, max(lmax, rmax))


def checkBST(root):
    if root is None:
        return True
    if root.data < minAndMax(root.left)[1] or root.data > minAndMax(root.right)[0]:
        return False
    return checkBST(root.left) and checkBST(root.right)


def checkBST2(root):
    if root == None:
        return 9999, -9999, True
    leftMin, leftMax, isLeftBST,  = checkBST2(root.left)
    rightMin, rightMax, isRightBST = checkBST2(root.right)
    minimum = min(root.data, leftMin, rightMin)
    maximum = max(root.data, leftMax, rightMax)
    isTreeBST = True
    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    if not (isLeftBST) or not (isRightBST):
        isTreeBST = False

    return  minimum, maximum,isTreeBST


root = treeInput()


levelOrderTraversal(root)
print()
print(checkBST2(root))
