def replaceWithPi(s):
    if len(s) == 0 or len(s) == 1:
      return s
    
    if s[0] =='P' and s[1] == 'i':
       small_string = replaceWithPi(s[2:])
       return "3.14" + small_string
    else:
       small_string = replaceWithPi(s[1:])
       return s[0] + small_string
    
s="pPipeline"
print(replaceWithPi(s))