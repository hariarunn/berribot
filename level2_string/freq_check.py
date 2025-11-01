s=input("enter the string:")
frq={}
for i in s:
    if i in frq:
        frq[i]+=1
    else:
        frq[i]=1
for key in frq:
    print(key,end="")
    print(frq[key],end="")