def changeChar(s,char1,char2):
    if len(s) == 0:
        return s 
    small_string= changeChar(s[1:],char1,char2)
    if s[0]==char1:
        return char2+ small_string
    else:
        return s[0] + small_string

s="atharva"
print(changeChar(s,"a","v"))    