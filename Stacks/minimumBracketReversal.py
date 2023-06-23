s="(((())"
def mbr(s):
    stack=[]
    c=0
    if len(s)%2!=0:
        return -1
    for i in s:
        if i=="(":
            stack.append(i)
        elif i==")":
            if len(stack)==0:
                stack.append(i)
                print(stack)
            elif len(stack)>0 and stack[-1]=="(":
                stack.pop()
            elif len(stack)>0 and stack[-1]==")":
                stack.append(i)
    while len(stack)>0:
        c1=stack.pop()
        c2=stack.pop()
        if c1==c2:
            c+=1
        else:
            c+=2
    return c


print(mbr(s))