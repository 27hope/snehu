#using isalpha
str1=str(input())
vowels=["a","e","i","o","u"]
if (str1.isalpha())==True:
    if str1 in vowels:
        print("Vowels")
    else:
        print("Consonant")

else:
    print("Invalid")
