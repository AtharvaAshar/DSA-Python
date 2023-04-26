class ListNode:
    def __init__(self,x):
        self.x = x
        self.next=None 


class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,value):
        new_node=ListNode(value)
        if(self.head):
            curr=self.head
            while(curr.next):
                curr=curr.next
            curr.next=new_node
        else:
            self.head=new_node
    
    def listToLL(self,l):
        for i in l:
            self.insert(value=i)
    def printLL(self):
        curr=self.head
        while(curr):
            print(curr.x)
            curr=curr.next
    def findNode(self,value):
        curr=self.head
        index=0
        while(curr.next):
            if curr.x==value:
                return index
            else:
                index+=1
                curr=curr.next
        
        

l=[1,2,3,4,5,6,7,8,9,10,11]
LL=LinkedList()
LL.listToLL(l)
print(LL.findNode(3))
# LL.printLL()



   
    


