for a in range(1,101):
    count=0
    for j in range(1,a+1):
        if a%j==0:
            count+=1
    if count==2:
        print(a)