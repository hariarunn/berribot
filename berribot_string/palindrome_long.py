s = input("Enter the string: ")
s = s.replace(" ", "").lower()
if s == s[::-1]:
    print(True)
else:
    print(False)
