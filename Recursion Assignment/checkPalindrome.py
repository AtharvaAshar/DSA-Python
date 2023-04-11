def checkP(s,si,ei):
    if si==ei:
        return True
    if s[si]!=s[ei]:
        return False
    
    return checkP(s,si+1,ei-1)
print(checkP("racecar",0,len('racecar')-1))
print(checkP("racecr",0,len('racecr')-1))
