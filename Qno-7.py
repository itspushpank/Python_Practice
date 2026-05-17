#write a program to check a substring is present in a given string or not.(Use Regular Expressions).
import re


string =input("Enter the String :")
substring =input("Enter the substiring you want to find :")

result= re.search(substring,string)

if result !=None:
    print(f"The substring '{substring}' is present in string '{string}'. ")
else:
    print(f"The substring '{substring}' is NOT present in string '{string}'. ")