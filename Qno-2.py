#Write a python program to find factorial of a number using Recursion. 

num= int(input(" Enter the number to find factorial : "))
def factorial(num):
    if num>=1:
        return num* factorial(num-1)
    else:
        return 1
    
print(f"factorial : {factorial(num)}")