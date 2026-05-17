#write a program to create tuple (name, age, address, college) for given no of members and print the tuple.
people= int(input("Enter the number of person you want to add :"))
tup1=[]
for j in range(1,people+1):
    
    l1=[]
    l1.append(input(f"Enter the person{j}'s Name : "))
    l1.append(int(input(f"Enter the person{j}'s age : ")))
    l1.append(input(f"Enter the person{j}'s Address : "))
    l1.append(input(f"Enter the person{j}'s College : "))
    # tup1+=tuple(l1)
    tup1.append(tuple(l1))

    
print(tuple(tup1))

