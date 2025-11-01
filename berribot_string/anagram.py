s1=input("enter the string: ")
s2=input("enter the string: ")
if sorted(s1.lower()) == sorted(s2.lower()):
    print("anagram")
else:
    print("not anagram")