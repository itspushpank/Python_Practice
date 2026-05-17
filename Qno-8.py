#write a program to only get list of even number from a given list of numbers.(use list comprehensions)

l1=[ x for x in range(1,101)]#list of number btw 1-100.

l2=[x  for x in l1 if x%2==0 ]
print(f"The list of Even no are :\n{l2}")