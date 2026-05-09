#Write a python program to find factorial of a number using Recursion. 

num= int(input(" Enter the number to find factorial : "))
def factorial(num):
    if num>=1:
        return num* factorial(num-1)
    if num<0:
        return "Does not exist(Negative no)!"
    else:
        return 1
    
print(f"factorial : {factorial(num)}")