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
def evenAfterOdd(head):
    oddHead,OddTail=None,None
    evenHead,evenTail=None,None
    while head is not None:
        if head.value %2 != 0:
            if oddHead is None:
                oddHead = head
                OddTail=head 
                head=head.next 
            else:
                OddTail.next=head
                OddTail=OddTail.next
                head=head.next
        else:
            if evenHead is None:
                evenHead = head
                evenTail=head 
                head=head.next 
            else:
                evenTail.next=head
                evenTail=evenTail.next
                head=head.next
    evenTail.next=None
    OddTail.next=evenHead
    return oddHead
   

head,l=takeinput()
printLL(head)
newhead=evenAfterOdd(head)
printLL(newhead)

