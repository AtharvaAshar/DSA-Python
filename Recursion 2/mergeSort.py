def merge(left,right,l):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l[k]=left[i]
            i+=1
            k+=1
        else:
            l[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
        l[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        l[k]=right[j]
        j+=1
        k+=1
    
def mergeSort(l):
    if len(l)==0 or len(l)==1:
        return
    mid = len(l)//2
    left=l[:mid]
    right=l[mid:]
    mergeSort(left)
    mergeSort(right)

    merge(left,right,l)


l=[3,2,1,4,5,6,7,11,10]

mergeSort(l)
print(l)