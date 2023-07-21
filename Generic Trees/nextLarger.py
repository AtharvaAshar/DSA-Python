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




def nextLarger(root,x):
    ans=None
    if not root: return ans
    if root.data>x:
        ans=root.data
    else: 
        ans=None
    for child in root.children:
        temp=nextLarger(child,x)
        if temp:
            if not ans or ans>temp:
                ans=temp

    return ans
    


root = levelwiseInput()
x=int(input("Enter x: "))

printLevelwise(root)
print()

print(nextLarger(root,x))
