def partition(l,si,ei):
    pivot=l[si]
    c=0
    for i in range(si,ei+1):
        if l[i]<pivot:
            c+=1
    l[si],l[si+c]=l[si+c],l[si]
    pivot_index=si+c
    i,j=si,ei
    while i<j:
        if l[i]<pivot:
            i+=1
        elif l[j]>pivot:
            j-=1
        else:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
    return pivot_index
            

def quickSort(l,si,ei):
    if si>ei:
        return 
    i=partition(l,si,ei) #pivot index
    quickSort(l,si,i-1)
    quickSort(l,i+1,ei)

l=[3,2,1,4,5,6,7,11,10]
print(quickSort(l,0,len(l)-1))
print(l)