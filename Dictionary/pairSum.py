def pairSum(l):
    d={}
    count = 0
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if -i in d:
            count+=d[i]*d[-i]
            d[i],d[-i]=0,0
        else:
            continue
    return count

def pairSum2(l):
    d={}
    count=0
    for i in l:
        if -i in d and i not in d and i!=0:
            count+=1
            d[i]=1
        elif -i in d and i!=0:
            count+=d[i]*d[-i]
            d[i] += 1
        elif i not in d:
            d[i]=1
        else:
            d[i]+=1
        
    return count

print(pairSum2([2,1,-2,2,3]))
print(pairSum2([-2,2,6,-2,2,-6,3,0,0]))

    