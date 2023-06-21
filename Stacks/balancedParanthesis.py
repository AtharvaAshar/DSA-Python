

stack=[]
string="(a+b{c-d)()"
def isBalanced(string):
    for s in string:
        if s=="(" or s=="{" or s=="[":
            stack.append(s)
        elif s=="}":
            if stack.pop()=="{":
                continue
            else:
                return False
        elif s==")":
            if stack.pop()=="(":
                continue
            else:
                return False
        elif s=="]":
            if stack.pop()=="[":
                continue
            else:
                return False
    
    if len(stack)>0:
        return False
    return True


print(isBalanced(string))