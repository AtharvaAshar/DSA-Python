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
def mergeSorted(head1,head2):
    fh,ft=None,None # final head and final tail
    if head1.value < head2.value:
        fh=head1
        ft=head1
        head1=head1.next
    else:
        fh=head2
        ft=head2
        head2=head2.next
    while head1 != None and head2 != None:
        if head1.value < head2.value:
            ft.next = head1
            ft=ft.next
            head1=head1.next
        else:
            ft.next=head2
            ft=ft.next
            head2=head2.next 
    if head1!=None:
        ft.next=head1
    else:
        ft.next=head2 
    return fh


head1,l1=takeinput()
head2,l2=takeinput()
printLL(head1)
printLL(head2)
new_head=mergeSorted(head1,head2)
printLL(new_head)