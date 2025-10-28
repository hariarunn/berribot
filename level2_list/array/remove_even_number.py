list1=list(map(int,input("enter the elements: ").split()))
odd =[]
for i in list1:
    if i%2==1:
        odd.append(i)
print(odd)
