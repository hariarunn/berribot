list1=list(map(int,input("enter the elements: ").split()))
even_position=[]
for i in range(len(list1)):
    if i % 2==0:
        even_position.append(list1[i])
print("Sum = ",sum(even_position))