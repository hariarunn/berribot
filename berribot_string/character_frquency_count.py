s=input("enter the string: ")
if s == "":
    print("")
else:
    result=""
    count=1 
    for ch in range(len(s)-1):
        if s[ch] == s[ch+1]:
            count+=1
        else:
            result += s[ch] +str(count)
            count= 1
    result += s[-1] +str(count)
    print(result)
        