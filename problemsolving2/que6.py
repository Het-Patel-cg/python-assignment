evenintegers = 0
oddintegers = 0

for i in range(1,6):
    num = int(input("enter an integer: "))
    if num % 2 == 0:
        evenintegers += 1
        print("even")
    else:
        oddintegers += 1
        print("odd")

if evenintegers > oddintegers:
    print("even")
elif oddintegers > evenintegers:
    print("odd")
else:
    print("equal")

print("even_integers", evenintegers)
print("odd_integers", oddintegers)