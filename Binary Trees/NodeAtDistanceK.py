from queue import Queue
import collections

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

def distanceKFromN(root,node,k):
    if root is None: return -1
    if root.data==node:
        printNodeAtK(root,k)
        return 0
    ld=distanceKFromN(root.left,node,k)
    if ld!=-1:
        if (ld+1)==k:
            print(root.data)
        else:
            printNodeAtK(root.right,k-ld-2)
        return ld + 1
    rd=distanceKFromN(root.right,node,k)
    if rd!=-1:
        if rd+1==k:
            print(root.data)
        else:
            printNodeAtK(root.left,k-rd-2)
        return rd + 1
    return -1

def distanceKFromN2(root,target,k):
        def dfs(node, parent):
                if node is None:
                    return
                node.parent = parent
                node.done = False
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root,None)
        
        q=collections.deque()
        q.append((target,0))
        target.done=True
        ans=[]

        while len(q)>0:
            node, d=q.popleft()
            if d==k:
                ans.append(node.val)
            print(node.left)
            for next_node in [node.left,node.right,node.parent]:
                if next_node !=None and  next_node.done!=True:
                    next_node.done=True
                    q.append((next_node,d+1))
                    
        return ans
    


root = treeInput()
target=int(input("Enter target: "))
k=int(input("enter distance: "))
levelOrderTraversal(root)
print()
distanceKFromN(root,target,k)
distanceKFromN2(root,target,k)

