s="this is string is made of words , it has many words is"
k=2

def getFrequentWord(s,k):
    d=dict()
    l=s.split(' ')
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    out=[]
    maximum=max(d.values())
   
    for i in d:
        if d[i]==maximum:
            out.append(i)
    return out
print(getFrequentWord(s,k))