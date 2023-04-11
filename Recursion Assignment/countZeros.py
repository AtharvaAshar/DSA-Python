def countZeros(n):
    if n==0:
        return 1
    if n<10:
        return 0
    elif n%10==0:
        return 1 + countZeros(n//10)
    return countZeros(n//10)
print(countZeros(102300))
