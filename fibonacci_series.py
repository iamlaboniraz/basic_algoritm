first_term=0
second_term=1
print(first_term)
print(end="")
print(second_term)

while second_term<=1000:
    temp = second_term
    second_term = second_term+first_term
    first_term = temp
    print(second_term)
