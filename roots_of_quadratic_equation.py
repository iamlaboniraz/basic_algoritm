import cmath

a = int(input("Enter the a's value = "))
b = int(input("Enter the b's value = "))
c = int(input("Enter the c's value = "))

D = b*2 - 4*a*c

if D>=0:
    r1 = (-b+cmath.sqrt(D))/(2*a)
    r2 = (-b-cmath.sqrt(D))/(2*a)
    print(f"r1 ={r1} and r2 = {r2}")
else:
    rp = b/2*a
    ip = cmath.sqrt(-D)/(2*a)
    print(rp+ip, "and", rp-ip)
