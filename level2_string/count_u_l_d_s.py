text=input("enter the string: ")
upper=0
lower=0
digit=0
special=0
for ch in text:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isnumeric():
        digit+=1
    else:
        special+=1
print("upper case: ",upper)
print("lower case: ",lower)
print("digits:",digit)
print("special characters",special) 
