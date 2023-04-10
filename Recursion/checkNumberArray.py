def checkNumber(n,l):
    if len(l)==0:
        return False
    if l[0]==n: return True
    return checkNumber(n,l[1:])
print(checkNumber(2,[4,2,3,4,5]))