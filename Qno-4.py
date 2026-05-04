#Write  a  Python  program  to  convert  temperatures  to  and  from  Celsius, Fahrenheit
print("--------------Celcius to Fahrenheit, vice-versa Calculator-------------")
print("Enter the choice -")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")
choice=input("\nEnter the choice:-").strip()
if choice == "1":
    cel=float(input("Enter the Celcius : "))
    print(f"Fahrenheit : {cel*9/5+32}")
elif choice == "2":
    far=float(input("Enter the Fahrenheit : "))
    print(f"Celcius : {(far-32)*5/9}")

else:
    print("Invalid choice!")