# 1.
for i in range(1, 5):
    if i == 1:
        break
    print(i)

print("End")

# OUTPUT:-


# 2.
for i in range(1, 7):
    print(i)
    if i == 4:
        break
print("Finished")


# OUTPUT:- 1
#          2
#          3
#          4


# 3.
for i in range(1, 7):
    print(i)
    if i == 4:
        break
print("Finished")

# OUTPUT:- 1
#          2
#          4
#          5

# 4.
for i in range(1, 5):
    if i == 2:
        pass
    print(i)


# OUTPUT:-
# 1
# 2
# 3
# 4

# 5.
for i in range(3):
    print("Python")
else:
    print("Done")


# OUTPUT:-
# Python
# Python
# Python

# 6.
for i in range(1, 5):
    print("A", i)
    if i == 3:
        break
    print("B", i)

# OUTPUT:-
# A 1
# B 1
# A 2
# B 2
# A 3
 
 
# 7.
for i in range(1, 5):
    if i == 2:
        continue
    print("Value:", i)
    print("Next line")

# OUTPUT:-
#  Value: 1
# Next line
# Value: 3
# Next line
# Value: 4
# Next line

# 8.
for i in range(1, 4):
    if i == 2:
        pass
        print("Inside if")
    print("Outside if", i)

# OUTPUT:-
# Outside if 1
# Inside if
# Outside if 2
# Outside if 3

# 9.
for i in range(2, 8, 2):
    print(i)
    if i == 4:
        break
    print("Hello")

print("After loop")


# OUTPUT:-
# 2
# Hello
# 4
# After loop


# 10.
for i in range(1, 5):
    print("Start", i)
    if i == 3:
        continue
    print("End", i)

# OUTPUT:-
# Start 1
# End 1
# Start 2
# End 2
# Start 3
# Start 4
# End 4


# 11.
for i in range(2, 5):
    print(i)
else:
    print("Loop completed")

# OUTPUT:-
# 2
# 3
# 4
# Loop completed

# 12.
for i in range(1, 6):
    if i == 4:
        break
    print(i)
else:
    print("Completed")
print("Program end")

# OUTPUT:-
# 1
# 2
# 3
# Program end


# 13.
for i in range(1, 5):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("Completed")

# OUTPUT:-
# 1
# 3
# Completed


# 14.
for i in range(5, 5):
    print(i)
else:
    print("Else executed")

# OUTPUT:-
# Else executed


# 15.
for letter in "CODE":
    print(letter)
    if letter == "D":
        break
else:
    print("All letters checked")

# OUTPUT:-
# C
# O
# D


# 16.
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
else:
    print("Finished normally")

# OUTPUT:-
# 1
# 2
# 3
# Finished normally


# 17.
word = "banana"

for ch in word:
    if ch == "n":
        print("Found")
        break
else:
    print("Not found")

# OUTPUT:-
# Found

# 18.
word = "apple"

for ch in word:
    if ch == "z":
        print("Found")
        break
else:
    print("Not found")

# OUTPUT:-
# Not found


# 19.
for ch in "education":
     if ch in "aeiou":
         continue
     print(ch, end="")
print()

# OUTPUT:-
# dctn

# 20.
for ch in "programming":
    if ch == "g":
        break
    print(ch, end="-")

# OUTPUT:-
# p-r-o-

# 21.
for ch in "computer":
    if ch == "o":
        continue
    if ch == "t":
        break
    print(ch, end="")

# OUTPUT:-
# cmpu

# 22.
for ch in "cat":
    if ch == "a":
        pass
    print(ch.upper(), end=" ")

# OUTPUT:-
# C A T 

# 23.
n = 1

while n <= 5:
    print(n)
    if n == 3:
        break
    n += 1

print("Stopped")

# OUTPUT:-
# 1
# 2
# 3
# Stopped

# 24.
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# OUTPUT:-
# 1
# 2
# 4
# 5


# 25.
n = 1

while n <= 5:
    if n == 2:
        n += 1
        continue
    print(n)
    n += 1

# OUTPUT:-
# 1
# 3
# 4
# 5


# 26.
n = 1

while n <= 4:
    if n == 3:
        break
    print(n)
    n += 1

print(n)

# OUTPUT:-
# 1
# 2
# 3


# 27.
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

# OUTPUT:-
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2



# 28.
for row in range(1, 3):
    for col in range(1, 4):
        if col == 2:
            continue
        print(row, col)

# OUTPUT:-
# 1 1
# 1 3
# 2 1
# 2 3


# 29.
for i in range(1, 4):
    print("Outer", i)
    for j in range(1, 4):
        if j == 2:
            break
        print("Inner", j)

# OUTPUT:-
# Outer 1
# Inner 1
# Outer 2
# Inner 1
# Outer 3
# Inner 1


# 30.
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
    else:
        print("Inner else", i)

# OUTPUT:-
# 1 1
# Inner else 1
# 2 1
# Inner else 2
# 3 1
# Inner else 3


# 31.
for i in range(1, 3):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
    else:
        print("Inner loop complete")

# OUTPUT:-
# 1 1
# 1 3
# Inner loop complete
# 2 1
# 2 3
# Inner loop complete

# 32.
for i in range(1, 7):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
else:
    print("Loop else")
print("End")

# OUTPUT:-
# 1
# 3
# 4
# End


# 33.
for i in range(1, 5):
    if i == 3:
        pass
    else:
        print("Else block", i)
    print("Number", i)

# OUTPUT:-
# Else block 1
# Number 1
# Else block 2
# Number 2
# Number 3
# Else block 4
# Number 4


# 34.
for i in range(1, 5):
    print("X", end="")
    if i == 2:
        continue
    print("Y", end="")
print("Z")

# OUTPUT:-
# XYXZYZ


# 35.
for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")

# OUTPUT:-
# 1
# 2
# Outside