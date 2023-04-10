def check_sorted(l):
    if len(l)==0 or len(l)==1:
        return True
    if l[0]>l[1]:
        return False    
    smallerlist_sorted=check_sorted(l[1:])
    if smallerlist_sorted:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,12,11]
# print(check_sorted(l))

def check_sorted_better(l,si):
    if si==len(l)-1 or si==len(l):
        return True
    if l[si]>l[si+1]:
        return False
    isSorted=check_sorted_better(l,si+1)
    return isSorted
print(check_sorted_better(l,0))