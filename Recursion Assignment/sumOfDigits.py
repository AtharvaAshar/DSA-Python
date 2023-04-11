def sumDigit(n):
    if n//10==0:
        return n
    return n%10 + sumDigit(n//10)

print(sumDigit(100))
print(sumDigit(1049))