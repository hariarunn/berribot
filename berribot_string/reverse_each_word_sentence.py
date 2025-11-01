s1 =input("enter the string:")
words=s1.split()
reversed_word=[]
for w in words:
    reversed_word.append(w[::-1])
result=" ".join(reversed_word)
print(result)