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

def reverseRecurBest(head):
    if head is None or head.next is None:
        return head
    smallhead=reverseRecurBest(head.next)
    tail=head.next 
    tail.next = head  
    head.next=None  
    return smallhead


head =takeinput()
printLL(head)
head =reverseRecurBest(head)
printLL(head)