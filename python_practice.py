<<<<<<< HEAD
# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))
#
# x = "  Thundersoft   "
#
# print(x.strip())

# x =[1,2,3,4]
#
# print(max(x))

x = "Main"
c =0

# print(x.isupper())

if x.isalnum():
    print('yes')

# for i in range(len(x)):
#     if x[i].islower() or x[i].isdigit() or x[i].isupper():
#         c+=i
#     else:
#         c=0
#
# if c > 0:
#     print("Valid Password")
# else:
#     print("Inavlid Password")

# A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# a = "abcdefghijklmnopqrstuvwxyz"
# num = "1234567890"
# inp = "Qwerty"
# c = 0
#
# for i in range(len(inp)):
#         if inp[i] in A:
#             c+=i
#         elif inp[i] in a:
#             c+= i
#         elif inp[i] in num:
#             c+= i
#         else:
#             c=0
# if c > 0:
#     print("Valid Password")
# else:
#     print("Inavlid Password")
#
# x ="Qwerty00"
# for i in range(len(x)):
#     if x[i].i

x = "Hello World"
c = ''
for i in range(len(x)):
    if x[i] in ['a','e','i','o','u']:
        c += ''
    else:
        c += x[i]

print(c)
=======
y = input('Enter the number:')
a = int()

for i in range(len(y)):
    a += int(y[i])**len(y)

if a==int(y):
    print('True')
else:
    print('False')
>>>>>>> master
