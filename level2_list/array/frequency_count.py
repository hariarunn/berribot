list1=list(map(int,input("enter the elements: ").split()))
freq={}
for ch in list1:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch]=1
for key in freq:
    print(key,":",freq[key])

