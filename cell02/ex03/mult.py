print("Enter the first number:")
a = int(input())
print("Enter the second number:")
b = int(input())
mult = a*b
if mult >0:
    print(a,"x",b,"=",mult)
    print("The result is positive.")
elif mult <0:
    print(a,"x",b,"=",mult)
    print("The result is negative.")
else:
    print(a,"x",b,"=",mult)
    print("The result is positive and negative.")