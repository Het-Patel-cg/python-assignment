
#1
for i in range(5):
 print("hello")
 #2
for i in range(10):
 print(i, end="")
#3
for i in range(1, 11):
 print(i, end="")
#4
for i in range(10, 0, -1):
 print(i, end="")
#5
for i in range(5, 51, 5):
 print(i, end="")
#6
for i in range(2, 21, 2):
 print(i, end="")
#7
for i in range(1, 20, 1):
 print(i, end="")
#8
for i in range(3, 19, 3):
 print(i, end="")
#9
for i in range(20, 1, -2):
 print(i, end="")
#10
n= int(input("enter a positive integer:"))
for i in range(1, n+1):
 print(i, end="")
#11
n= int(input("enter n: "))
for i in range(1, n+1):
 if 1 % 2 == 0:
  print(i, end="")
#12
n= int(input("enter n: "))
for i in range(1, n+1):
 if 1 % 2 != 0:
  print(i, end="")
#13
n= int(input("enter n: "))
for i in range(1, n+1):
 if i % 3 == 0:
  print(i, end="")
#14
n= int(input("enter n: "))
for i in range(1, n+1):
 if 1 % 2 == 0 and 1 % 3 == 0:
  print(i, end="")
#15
n= int(input("enter n: "))
for i in range(1, n+1):
 if 1 % 2 == 0:
  count+= 1
  print("even numbers count:", count)
#16
n= int(input("enter n: "))
total=0
for i in range(1, n+1):
 total= total+i
 print("sum =", total)
#17
n= int (input("enter even n: "))
total=0
for i in range(2, n+2, 2):
 total= total+i
 print("sum =", total)
#18
n= int(input("enter odd n: "))
total=0
for i in range(1, n+1, 1):
 total= total+i
print("sum =", total)
#19
num= int(input("enter a num: "))
for i in range(1,11):
 print("multiplication =", num*i)
#20
n= int(input("enter n: "))
product= 1
for i in range(1, n+1):
 product= product*i
 print("product =", product)
#21
s= input("enter a string: ")
for ch in s:
 print(ch)
#22
s= input("enter a string:")
for ch in s:
 print(ch, end="")
#23
s= input("enter a string:")
count=0
for ch in s:
 count= count+1
 print("count:", count)
#24
s= input("enter a string: ")
count=0
for ch in s:
 if ch == 'a':
  count= count+i
  print("count:", count)
#25
s = input("enter a string: ")
count = 0
for ch in s:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count += 1
print("uppercase count =", count)
#26
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()
#27
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()
#28
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
#29
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
#30
for i in range(1, 6):
    for j in range(1, 6):
        print(i*j, end="\t")
    print()