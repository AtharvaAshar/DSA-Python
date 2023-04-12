def sti(s):
    if len(s) == 0:
        return 0
    a=int(s[0])
    a*=pow(10,len(s)-1)
    return a + sti(s[1:])

print(sti("12345"))
