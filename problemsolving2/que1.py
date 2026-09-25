char = (input("enter a string"))
upper = 0
lower = 0
digit = 0
space = 0
special = 0


for ch in char:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        special += 1

print("uppercase:", upper)
print("lowercase:", lower)
print("digits:", digit)
print("spaces", space)
print("special",special)
    