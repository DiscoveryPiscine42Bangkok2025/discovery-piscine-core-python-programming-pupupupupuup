print("Enter a number less than 25")
n = int(input())
if n > 25 :
    print("Error")
else:
    for i in range(n,25+1):
        print("Inside the loop, my variable is",i)
        i+=1