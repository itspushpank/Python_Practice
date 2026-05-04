"""Write a Program to display all prime numbers within an interval of 20 and 50. """

for i in range(20,51):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(f"{i} is prime number")
