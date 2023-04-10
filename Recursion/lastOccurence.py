def last_index(l,li,n):
    if li==0:
        return -1
    if l[li]==n:
        return li
    return last_index(l,li-1,n)

l=[1,2,3,4,5,4,1,2,4]
print(last_index(l,len(l)-1,1))


def last_index_new_method(l,n):
    if len(l)==0:return -1
    if l[-1]==n:
        return len(l)-1
    small_list_output=last_index_new_method(l[:-1],n)
    if small_list_output==-1:
        return -1
    else:
        return small_list_output
print(last_index_new_method(l,5))