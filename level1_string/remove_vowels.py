n=input("enter the string to remove vowels: ")
vow="aeiouAEIOU"
for i in n:
    if i not in vow:
        print(i ,end="") 