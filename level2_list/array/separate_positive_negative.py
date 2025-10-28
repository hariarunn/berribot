list1=list(map(int,input("enter the elements: ").split()))
positive= []
negative=[]
for i in list1:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
print("Positive: ",positive)
print("Negative: ",negative)