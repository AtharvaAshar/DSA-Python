class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
def takeinput():
    inputList = [int(elem) for elem in input("Enter Linked list: ").split()]
    l=len(inputList)
    head=None
    for currData in inputList:
        if currData== -1:
            break 
        newNode = Node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next != None:
                curr=curr.next
            curr.next=newNode
    return head,l

def printLL(head):
    if head is None or head.next is None:
        return head
    else:
        while head is not None:
            print(str(head.value)+"->",end=" ")
            head = head.next
        print(None)
    return
def midPoint(head,l):
    slow,fast=head,head
    while fast.next!=None and fast.next.next != None:
            slow=slow.next
            fast=fast.next.next
    print(slow.value)
   

head,l=takeinput()
printLL(head)
midPoint(head,l-1)
