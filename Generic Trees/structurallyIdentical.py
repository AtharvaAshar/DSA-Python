from queue import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def levelwiseInput():
    q = Queue()
    root = int(input("Enter root data "))
    if root == -1:
        return None
    root = TreeNode(root)
    q.put(root)
    while not (q.empty()):
        curr = q.get()
        n = int(input(f"Enter number of children of {curr.data}"))
        for i in range(n):
            child = TreeNode(int(input(f"enter child {i+1} of {curr.data}")))
            curr.children.append(child)
            q.put(child)
    return root


def printLevelwise(root):
    q = Queue()
    q.put(root)
    q.put(None)
    print()
    while not (q.empty()):
        curr = q.get()
        if curr is not None:
            print(curr.data, end=":")
            for child in curr.children:
                q.put(child)
                print(child.data, ",", end=" ")
        else:
            if q.empty():
                break
            else:
                print()
                q.put(None)


def countNodeLargerThanX(root, x):
    c = 0
    if root.data > x:
        c = 1
    return c + sum(countNodeLargerThanX(child, x) for child in root.children)


def identical(root1,root2):
    if not root1:
        if not root2:
            return True
        return False
    if root1.data!=root2.data or len(root1.children)!=len(root2.children):
        return False
    else:
        for child1,child2 in zip(root1.children,root2.children):
                if not identical(child1,child2):
                    return False
    return True



root1 = levelwiseInput()
root2 = levelwiseInput()

printLevelwise(root1)
print()
printLevelwise(root2)
print()
print(identical(root1, root2))
