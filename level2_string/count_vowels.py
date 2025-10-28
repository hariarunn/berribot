n=input("enter the string: ")
vow="aeiouAEIOU"
count=0
for i in n:
    if i in vow:
        count+=1
print("the number of vowels is: ",count)
    