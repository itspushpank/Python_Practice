#Write a program to print Fibonacci sequence using while loop.
n=int(input("Enter the no of terms onto which you want fibo series"))
count=0
a,b=0,1
while count <= n:
    count+=1
    if count==1:
        print(0)
    elif count==2:
        print(1)
    else:
        temp=b
        b=a+b
        a=temp
        print(b)