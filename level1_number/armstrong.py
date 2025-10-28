num=int(input("enter the number: "))
temp=num
sum =0
while num>0:
    digit= num%10
    sum+=digit**3
    num=num//10
if (sum==temp):
    print("armstrong")
else:
    print("not a armstrong")