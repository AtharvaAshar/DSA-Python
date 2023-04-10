def removeDuplicates(s):
    if len(s) ==0 or len(s) ==1:
        return s 
    small_string = removeDuplicates(s[1:])
    if s[0] == s[1]:
       return  small_string
    else:
       return s[0] + small_string
    
s="aabcdaa"

print(removeDuplicates(s))