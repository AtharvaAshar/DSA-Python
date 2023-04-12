def staircase(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    return  staircase(n-1) + staircase(n-3) +staircase(n-2)
    
print(staircase(4))