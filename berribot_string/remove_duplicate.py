s1=input("enter the string:")
result=""
for ch in s1:
    if ch not in result:
        result+=ch 
print(result)