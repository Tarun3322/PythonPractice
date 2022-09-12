x = "Hello World"
c = ''
for i in range(len(x)):
    if x[i] in ['a','e','i','o','u']:
        c += ''
    else:
        c += x[i]

print(c)