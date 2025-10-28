letter=input("enter the string: ")
for ch in letter:
    if letter.count(ch)==1:
        print(ch)
        break 
    