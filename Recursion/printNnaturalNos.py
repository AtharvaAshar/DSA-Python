def n_natural(n):
    if n==0:
        return 
    n_natural(n-1)
    print(n)
    return 

#n_natural(9)

def n_to_1_natural(n):
    if n==0:
        return
    print(n)
    n_to_1_natural(n-1)
    return

n_to_1_natural(9)