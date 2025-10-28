text=input("enter the string: ")
result=""
for i in text:
    if i.isalnum() or i.isspace():
        result += i
print(result)