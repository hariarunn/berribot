n=input("enter the string: ")
for i in range(0,len(n)):
    for j in range(i+1,len(n)+1):
        print(n[i:j])