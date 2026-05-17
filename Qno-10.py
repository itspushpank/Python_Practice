#Write a program to return the top 'n'most frequently occurring chars and their respective counts.
#eg. aaaaaaaaabbbbbbccccc -> [(a,9),(b,6),(c,5)]

str1=input("Enter the string :")
count=1
lst=[]
for i in range(len(str1)):
    if i < len(str1)-1 and str1[i] == str1[i+1]:
        count+=1
    else:
        lst.append((str1[i],count))
        count=1
print(lst)