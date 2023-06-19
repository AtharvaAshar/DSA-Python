class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
def takeinput():
    inputList = [int(elem) for elem in input("Enter Linked list: ").split()]
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
    return head

def printLL(head):
    if head is None or head.next is None:
        return head
    else:
        while head is not None:
            print(str(head.value)+"->",end=" ")
            head = head.next
        print(None)
    return


def kReverse(head,k):
    if k==0 or k==1:
        return head 
    prev=None
    curr=head
    fwd=None
    c=0
    while c<k and curr is not None:
        fwd=curr.next
        curr.next=prev 
        prev=curr
        curr=fwd 
        c+=1 

    if fwd is not None:
        head.next=kReverse(fwd,k) 
    return prev
    


head =takeinput()
printLL(head)
new_head=kReverse(head,3)
printLL(new_head)