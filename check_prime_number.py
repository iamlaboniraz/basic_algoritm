n = int(input("Enter the number = "))
flag=1
if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                flag =0
                if flag == 0:
                    print("not prime")
                    break
        else:
            print("prime")
else:
    print("not prime")

    
    
   


