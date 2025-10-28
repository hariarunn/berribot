list1=list(map(int,input("enter the elements: ").split()))
list2=list(map(int,input("enter the elements: ").split()))
common = list(set(list1) & set (list2))
print(common)