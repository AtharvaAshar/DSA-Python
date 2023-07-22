from queue import Queue
from collections import deque

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



def replaceDepth(root):
    q=deque()
    q.append((root,0))
    while q:
        for i in range(len(q)):
            curr,depth=q.popleft()
            curr.data=depth
            for child in curr.children:
                q.append((child,depth+1))
    
def replaceDepth2(root):
    def helper(root,depth):
        root.data=depth
        for child in root.children:
            helper(child,depth+1)
        
    helper(root,0)


root = levelwiseInput()
printLevelwise(root)
print()

replaceDepth(root)
printLevelwise(root)