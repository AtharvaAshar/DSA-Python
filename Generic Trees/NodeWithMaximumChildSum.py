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

def countNodeLargerThanX(root,x):
    c=0
    if root.data>x:
        c=1
    return c + sum(countNodeLargerThanX(child,x) for child in root.children)


def nodeWithMaxChildSum(root):
    childSum=root.data
    
    ans=root
    for child in root.children:
        childSum+=child.data
    for child in root.children:
        node=nodeWithMaxChildSum(child)
        callChild = node.data
        for child in node.children:
            callChild+=child.data
        if callChild>childSum:
            ans=node
    return ans
  
def nodeWithMaxChildSum2(root):
    if not root:
        return None,0
    maxNode,maxSum=root,root.data + sum(child.data for child in root.children)
    for child in root.children:
        childNode,childSum=nodeWithMaxChildSum2(child)
        currentSum=child.data + childSum
        if currentSum>maxSum:
            maxNode,maxSum=childNode,childSum
    return maxNode,maxSum
        
    

root=levelwiseInput()

printLevelwise(root)
print()
print(nodeWithMaxChildSum(root).data)
ans, sumAnswer=nodeWithMaxChildSum2(root)
print(ans.data)