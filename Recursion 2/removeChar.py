def remove_char(s,char):
    if len(s)==0:
        return s
    small_string = remove_char(s[1:],char)
    if s[0]== char:
        return small_string
    else:
        return s[0]+small_string

s="atharva ashar" 
print(remove_char(s,"a"))