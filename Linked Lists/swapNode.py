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
    c1,c2=0,0
    p1,p2=head,head
    while c1<i:
        c1+=1
        p1=p1.next
    while c2<j:
        c2+=1
        p2=p2.next
    d1,d2=p1.value,p2.value
    p1.value,p2.value=d2,d1 

    return head

head,l=takeinput()
printLL(head)
new_head=swap(head,0,2)
printLL(new_head)
