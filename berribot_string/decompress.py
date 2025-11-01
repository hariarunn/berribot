s1=input("enter the string: ")
result=""
for i in range(0,len(s1),2):
    char = s1[i]
    count=int(s1[i+1])
    result+=char*count 
print(result)