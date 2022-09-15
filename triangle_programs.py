# Basic Triangle
n = input("Enter one Number: ")
for i in range(1,int(n)+1):
    print((i * "* ").center(2*int(n),' '))

# Right Triangle
n = input("\nEnter one Number: ")
for i in range(1,int(n)+1):
    print(i * "* ")