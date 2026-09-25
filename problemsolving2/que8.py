budget = 0
regular = 0
luxury = 0
premium = 0
total = 0         

for i in range(8):
    price = float(input("enter product price: "))
    total += price

    if price < 500:
        budget += 1
    elif price < 1999:
        regular += 1
    elif price < 5000:
        premium += 1
    else:
        luxury += 1

average = total / 8

print("budget friendly", budget)
print("regular price", regular)
print("luxury price", luxury)
print("premium price", premium)
print("total price", total)
print("average price", average)