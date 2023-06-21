stock=[60,70,80,100,90,75,80,120]

def stockSpan(stock):
    stack=[]
    stack.append(0)
    output = [-1] * len(stock)
    output[0]=1
    for i in range(1,len(stock)):
       while len(stack)!=0 and stock[i]>stock[stack[-1]]:
            stack.pop()
       if len(stack)==0:
           output[i]=i+1
       else:
           output[i]=i-stack[-1]
       stack.append(i)
    return output
print(stockSpan(stock))
