s1=[1,2,3,4]
s2=[]
def reverseStack(s1,s2):
    if len(s1)==1:
        return 
    for i in range(len(s1)-1):
        s2.append(s1.pop())
    temp=s1.pop()
    for i in range(len(s2)):
        s1.append(s2.pop())
    reverseStack(s1, s2)
    s1.append(temp)
    return s1

print(reverseStack(s1, s2))
