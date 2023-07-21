from queue import Queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
def printRecursive(root):
    if root is None: #not a base case
        return 
    print(root.data, ":" ,end=" ")
    for child in root.children:
        print(child.data, "," ,end=" ")
    for child in root.children:
        print()
        printRecursive(child)
    
def inputTree():
    nodeData = int(input("Enter node data : "))
    if nodeData==-1: return None #not a base case
    node=TreeNode(nodeData)
    n=int(input(f"Enter number of children of {nodeData} : "))
    
    for i in range(n):
        child=inputTree()
        node.children.append(child)
    
    return node
def countNodes(root):
    if root==None:
        return 0
    return 1 + sum(countNodes(child) for child in root.children)
def sumOfAllNodes(root):
    if root==None:
        return 0
    return root.data +sum(sumOfAllNodes(child) for child in root.children)

def largestNode(root):
    if root==None:
        return None
    largest=root.data
    for child in root.children:
        largest=max(largest,largestNode(child))
    return largest


def largestNode2(root):
    return None if root is None else root.data if not root.children else max(root.data, *(largestNode2(child) for child in root.children))

def height(root):
    if root is None:
        return 0
    maxHeight=0
    for child in root.children:
        maxHeight=max(maxHeight,height(child))
    return 1 + maxHeight

def height2(root):
    return 0 if root is None else 1 if not root.children else 1 + max(0, *(height2(child) for child in root.children))

def levelwiseInput():
    q = Queue()
    root=int(input("Enter root data "))
    if root ==-1:
        return None
    root = TreeNode(root)
    q.put(root)
    while not (q.empty()):
        curr = q.get()
        n=int(input(f"Enter number of children of {curr.data}"))
        for i in range(n):
            child = TreeNode(int(input(f"enter child {i+1} of {curr.data}")))
            curr.children.append(child)
            q.put(child)
    return root

def printLevelwise(root):
    q=Queue()
    q.put(root)
    q.put(None)
    print()
    while not (q.empty()):
        curr=q.get()
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


n1=TreeNode(5)
n2=TreeNode(2)
n3=TreeNode(9)
n4=TreeNode(8)
n5=TreeNode(7)
n6=TreeNode(15)
n7=TreeNode(1)
n9=TreeNode(10)


n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)

n7.children.append(n9)

# print(countNodes(n1))
# print(sumOfAllNodes(n1))
# print(largestNode2(n1))
root=levelwiseInput()
print(height2(root))
printLevelwise(root)
# root=inputTree()
# printRecursive(root)