n=input("enter the string: ").strip()
count=0
for i in n:
    if i == " ":
        count+=1
print("spaces:", count)