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
    def reverseLL(self):
        prev=None
        while self.head:
            curr=self.head
            self.head=self.head.next
            curr.next=prev
            prev=curr
        self.head=prev
        



l=[1,2,3,4,5]
LL=LinkedList()
LL.listToLL(l)

LL.reverseLL()
LL.printLL()
