n=input("enter the string: ")
vow="aeiouAEIOU" 
v=0
c=0
for i in n:
    if i.isalpha():
        if i in vow:
            v+=1
        else:
            c+=1
print("vowels: ",v)
print("consonants: ",c)