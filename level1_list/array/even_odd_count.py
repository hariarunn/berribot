list1=list(map(int,input("enter the list: ").split()))
even_count=0
odd_count=0
for i in list1:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even: ",even_count)
print("Odd: ",odd_count)
