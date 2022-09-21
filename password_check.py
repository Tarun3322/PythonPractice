A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sp = "!@#$%^&*()_+-=;:'\""
inp = input("Enter your password with a small letters, capital letters, special character and size of 8: ")
x = y = z = s = False


for i in inp:
    if i in A:
        x = True
    if i in a:
        y = True
    if i in num:
        z = True
    if i in sp:
        s = True


if x == True and y == True and z == True and s == True and len(inp) >= 8:
    print("Valid Password")
else:
    print("Inavalid Password")