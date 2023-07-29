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
def swap(head,i,j):
    if i==j:
        return head
    p1=None 
    c1=head 
    p2=None 
    c2=head 
    for _ in range(i):
        p1=c1 
        c1=c1.next 
    for _ in range(j):
        p2=c2 
        c2=c2.next 
    if p1!=None:
        p1.next=c2 
    else:
        head=c2 
    if p2!=None:
        p2.next=c1 
    else:
        head=c1 
    c1.next,c2.next=c2.next,c1.next
    return head 


head,l=takeinput()
printLL(head)
new_head=swap(head,0,2)
printLL(new_head)
