s1=input("enter the string: ")
words=s1.split()
freq ={}
for ch in words:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch]=1
for key in freq:
    print(key,":",freq[key])
