s1=input("enter the string1: ").strip()
s2=input("enter the string2: ").strip()
if len(s1) == len(s2):
    if s2 in (s1 + s1):
        print("true")
    else:
        print("false")