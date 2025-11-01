s1 =input("enter the string: ")
vowel="aeiouAEIOU"
vow=0
con=0
for ch in s1:
    if ch.isalpha():
        if ch in vowel:
            vow+=1
        else:
            con+=1
print("Vowels:",vow)
print("Consonants:",con)
