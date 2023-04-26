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

    def removeDuplicates(self):
        curr=self.head
        # if self.head==None or self.head.next==None:
        #     return 
        while (curr is not None):
            next_node=curr.next
            if next_node is  None or next_node.value!= curr.value:
                curr=next_node
            else:
                curr.next=next_node.next
        



l=[1,2,3,4,5,5,6,7,8,9,9,10,11]
LL=LinkedList()
LL.listToLL(l)
LL.removeDuplicates()
print(LL.printLL())
