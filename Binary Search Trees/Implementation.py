class BTnode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
        self.numNode=0
    
    def isPresentHelper(self,root,data):
        if self.root is None:
            return False
        if self.root.data == data:
            return True
        if data < self.root.data:
            return self.isPresentHelper(self,root.left,data)
        else:
            return self.isPresentHelper(self,root.right,data) 
    def search(self,node):
        return self.isPresentHelper(self.root,node)
    def printTreeHelper(self,root):
        if root is None:
            return
        print(root.data, end=":")
        if root.left is not None:
            print("L", root.left.data, end=",")
        if root.right is not None:
            print("R", root.right.data, end=" ")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    def insertHelper(self,root,data):
        if root ==None:
            return BTnode(data)
        if root.data<=data:
            root.right=self.insertHelper(root.right,data)
            return root
        else:
            root.left = self.insertHelper(root.left, data)
            return root
    def insert(self,data):
        self.numNode+=1
        self.root= self.insertHelper(self.root,data)
    def minimum(self,root):
        if root is None:
            return 10**20
        if root.left  is None:
            return root.data
        return self.minimum(root.left)
    def deleteTreeHelper(self,root,data):
        if root is None:
            return False,None
        if root.data<data:
            deleted,newRight=self.deleteTreeHelper(root.right,data)
            root.right=newRight
            return deleted,root
        elif root.data>data:
            deleted,newLeft=self.deleteTreeHelper(root.left,data)
            root.left=newLeft
            return deleted,root
        else:
            if root.left is None and root.right is None:
                return True,None
            elif root.left is not None and root.right is None:
                return True,root.left
            elif root.right is not None and root.left is None:
                return  True,root.right
            else:
                replacement=self.minimum(root.right)
                root.data=replacement
                deleted,newRightNode=self.deleteTreeHelper(root.right,replacement)
                root.right=newRightNode
                return True,root
        
        
    def deleteData(self,data):
        deleted,new_root = self.deleteTreeHelper(self.root, data)
        if deleted:
            self.numNode -= 1
        self.root = new_root
        return deleted
    def count(self):
        return self.numNode
    

b=BST()
b.insert(10)
b.insert(5)
b.insert(12)
print(b.search(10))
print(b.count())
b.deleteData(5)
b.printTree()

