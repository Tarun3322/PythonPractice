x = input("Enter the String:")

c=0

for i in range(len(x)):
    if x[i].casefold() == x[len(x)-(i+1)].casefold():
        c+=i
    else:
        c=0

if c > 0:
    print('True')
else:
    print('False')