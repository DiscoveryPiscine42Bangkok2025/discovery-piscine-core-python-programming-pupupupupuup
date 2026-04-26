x = input("")
alp = "abcdefghijklmnopqrstuvwxyz"

result = ""

for i in x:
    if i in alp:
        result += i.upper()
    else:
        result += i.lower()

print(result)