a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))
c = int(input("Enter the third number = "))

if a>b:
    if a>c:
        print("a is largest number and number is = ",a)
    else:
        print("c is largest number and number is = ",c)
else:
    if b>c:
        print("b is largest number and number is = ",b)
    else:
        print("c is largest number and number is = ",c)
