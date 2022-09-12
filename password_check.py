A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sp = "!@#$%^&*()_+-=;:'\""
inp = "Qwerty@00"
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


if x == True and y == True and z == True and s == True:
    print("Valid Password")
else:
    print("Inavalid Password")