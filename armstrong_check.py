y = input('Enter the number:')
a = int()

for i in range(len(y)):
    a += int(y[i])**len(y)

if a==int(y):
    print('True')
else:
    print('False')