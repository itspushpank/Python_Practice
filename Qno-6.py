# Write a program to check two strings are anagrams or not.
s1=input("Enter the string 1 :")
s2=input("Enter the string 2 :")

check=True
if len(s1.replace(" ","")) == len(s2.replace(" ","")):
    for i in s1.replace(" ","").lower():
        if i not in s2.replace(" ","").lower():
            check=False
if check==True:
    print(f"'{s1}' and '{s2}' are Anagrams.")       
else:
    print(f"'{s1}' and '{s2}' are NOT Anagrams.")