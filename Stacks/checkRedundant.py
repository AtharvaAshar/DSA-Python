string="(a+b)((c+d))"
stack=[]
def checkRedundant(string):
    for i in range(len(string)):
        if string[i] !=")":
            stack.append(string[i])
        elif string[i] ==")":
            hasOperator= False 
            while len(stack)>0 and stack[-1]!="(":
                stack.pop()
                hasOperator=True 
            if not hasOperator:
                return True 
            if len(stack)>0:
                stack.pop()
    return False
                
print(checkRedundant(string)) 
    
