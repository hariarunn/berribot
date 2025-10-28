list1=list(map(int,input("List: ").split()))
s=int(input("Search: "))
if s in list1:
    print("Element found ")
else:
    print("Element not found ")

