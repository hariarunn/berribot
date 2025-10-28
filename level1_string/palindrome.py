n=input("enter the string to check palindrome: ")
rev= n[::-1]
if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")