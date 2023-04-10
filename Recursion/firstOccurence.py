def first_index(l,si,n):
    if si==len(l):
        return -1
    if l[si]==n:
        return si
    return first_index(l,si+1,n)

l=[1,2,3,4,5,4]
print(first_index(l,0,4))

def first_index_new_method(l,n):
    if len(l)==0:return -1
    if l[0]==n:
        return 0
    small_list_output=first_index_new_method(l[1:],n)
    if small_list_output==-1:
        return -1
    else:
        return small_list_output+1
print(first_index_new_method(l,4))