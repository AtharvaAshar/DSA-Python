def binary_search(l,si,ei,n):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if n<l[mid]:
        return binary_search(l,si,mid-1,n)
    elif n>l[mid]:
        return binary_search(l,mid+1,ei,n)
    else:
        return mid 

l=[1,2,3,4,5,6,7,8,10,9,11]
l.sort()
print(l)
print(binary_search(l,0,len(l)-1,9))