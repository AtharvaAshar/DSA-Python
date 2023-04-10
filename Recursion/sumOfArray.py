def SumArray(a):
    if len(a) == 0:
        return 0
    output=a[0]
    return output+SumArray(a[1:])
print(SumArray([1,2,3,4,5,10]))
