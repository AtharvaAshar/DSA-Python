    p1,c1=None,head
    p2,c2=None,head
    for i in range(i):
        p1=c1
        c1=c1.next 
    for i in range(j):
        p2=c2
        c2=c2.next 
    p1.next=c2
    p2.next=c1
    c1.next=c2.next 
    c2.next=p2 