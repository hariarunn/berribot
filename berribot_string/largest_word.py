s=input("enter the string: ")
largest=""
words=s.split()
for i in words:
    if len(i)>len(largest):
        largest=i 
print(largest)