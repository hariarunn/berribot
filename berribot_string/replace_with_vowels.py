s1=input("enter the string: ")
vowels="aeiouAEIOU"
result=""
for ch in s1:
    if ch in vowels:
        result+="#"
    else:
        result+=ch 
print(result)