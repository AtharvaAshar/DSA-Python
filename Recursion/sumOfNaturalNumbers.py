def sumation(n):
    if n==0:
        return 0
    return n + sumation(n-1)

print(sumation(5))