def check_ab(s):
    if len(s)==0:
        return True
    if s[0]=="a":
        if len(s)==1:
            return True
        elif s[1]=="a":
            return check_ab(s[1:])
        elif len(s)>=3 and s[1:3]=="bb":
            return check_ab(s[2:])
        else:
            return False
    elif s[0]=="b":
        if len(s)==1:
            return True
        elif s[1]=="a":
            return check_ab(s[1:])
        else:
            return False

def main(s):
    if s[0]=="a":
        return check_ab(s)
    else:
        return False

print(main("abababa"))