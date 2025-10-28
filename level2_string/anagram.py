text1=input("string1: ")
text2=input("string2: ") 
if sorted(text1.lower()) == sorted(text2.lower()):
    print("anagram")
else:
    print("not anagram")
