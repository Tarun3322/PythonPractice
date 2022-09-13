n = input("Number of Terms:")
a, b = 0, 1
print('Fibonacci Series: \n{}\n{}'.format(a,b))
for i in range(int(n)-2):
    c = a + b
    print(c)
    a = b
    b = c