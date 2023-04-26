class ListNode:
    def __init__(self,value):
        self.value = value
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
            print(curr.value)
            curr=curr.next
    
    def appendLastN_at_beg(self,n):
        curr=self.head
        length=0
        while(curr.next):
            curr=curr.next
            length+=1
        tail=curr
        curr=self.head
        for _ in range(length-n):
            
            curr=curr.next
        tail.next=self.head
        self.head=curr.next
        curr.next=None

        

        

l=[1,2,3,4,5,6,7,8,9,10,11]
LL=LinkedList()
LL.listToLL(l)
LL.appendLastN_at_beg(3)
LL.printLL()