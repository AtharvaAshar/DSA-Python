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
def deleteMafterN(head,m,n):
    curr=head 
    temp=None 
    while curr is not None:
        take,skip=0,0 
        while curr is not None and take <n:
            if temp is None:
                temp = curr 
            else :
                temp.next=curr
                temp=curr 
            curr=curr.next
            take+=1 
        while curr is not None and skip <m:
            curr=curr.next
            skip+=1 
    if temp is not None:
        temp.next=None 
    return head 
           

head,l=takeinput()
printLL(head)
newhead=deleteMafterN(head,2,2)
printLL(newhead)

