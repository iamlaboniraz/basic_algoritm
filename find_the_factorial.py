n = int (input("Enter the number = "))
factorial = 1
i=1
if n<0:
    print("does not exist!!")
else:
    for i in range(1,n+1):
        factorial = factorial*i
    print(factorial)
 
    
