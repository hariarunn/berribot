s1=input("enter the string: ")
result=""
for ch in s1:
    if ch.isalnum() or ch.isspace():
        result+=ch 
print(result)