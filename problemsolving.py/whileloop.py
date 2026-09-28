#1
i = 1
while i <= 5:
    print("Hello")
    i += 1

#2
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

#3
i = 1
while i <= 10:
    print(i)
    i += 1


#4
i = 10
while i >= 1:
    print(i)
    i -= 1

#5
i = 5
while i <= 50:
    print(i)
    i += 5

#6
i = 2
while i <= 20:
    print(i)
    i += 2

#7
i = 1
while i <= 19:
    print(i)
    i += 2

#8
i = 3
while i <= 18:
    print(i)
    i += 3


#9
n = int(input("Enter a positive integer: "))
i = 1
while i <= n:
    print(i)
    i += 1


#10
n = int(input("Enter a positive integer: "))
i = 1
while i <= n:
    print(i)
    i += 1


#11
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


#12
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1


#13
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1


#14
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i += 1


#15
n = int(input("Enter n: "))
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1
print("Even count =", count)


#16
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)


#17
n = int(input("Enter n: "))
i = 2
total = 0
while i <= n:
    total += i
    i += 2
print("Sum of evens =", total)


#18
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 2
print("Sum of odds =", total)


#19
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


#20
n = int(input("Enter n: "))
i = 1
product = 1
while i <= n:
    product *= i
    i += 1
print("Product =", product)


#21
s = input("Enter a string: ")
i = 0
while i < len(s):
    print(s[i])
    i += 1

#22
s = input("Enter a string: ")
i = 0
while i < len(s):
    print(s[i], end="")
    i += 1


#23
s = input("Enter a string: ")
i = 0
count = 0
while i < len(s):
    count += 1
    i += 1
print("Length =", count)

#24
s = input("Enter a string: ")
i = 0
count = 0
while i < len(s):
    if s[i] == "a":
        count += 1
    i += 1
print("Count of 'a' =", count)


#25
s = input("Enter a string: ")
i = 0
count = 0
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while i < len(s):
    if s[i] in uppercase:
        count += 1
    i += 1
print("Uppercase count =", count)


#26
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print("*", end="")
        j += 1
    print()
    i += 1


#27
i = 1
while i <= 4:
    j = 1
    while j <= 5:
        print("*", end="")
        j += 1
    print()
    i += 1


#28
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1


#29
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1


#30
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
