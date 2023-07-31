def unique(s):
    d=set()
    out=""
    for c in s:
        if c not in d:
            d.add(c)
            out+=c
        else:
            continue
    return out
print(unique("aabbccdeded"))