'''Given a string S, compute recursively a
 new string where identical chars that are adjacent in the original string are separated from each other by a "*".'''

def pairStar(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==s[1]:
        return s[0]+"*" + pairStar(s[1:])
    else:
       return s[0] + pairStar(s[1:])
print(pairStar("abaabb"))