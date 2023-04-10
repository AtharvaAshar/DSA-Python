def fib(n):
    if n==1 or n==2:
        return 1
    output=fib(n-1)+fib(n-2)
    
    return output

for i in range(1,10):
    print(fib(i))
