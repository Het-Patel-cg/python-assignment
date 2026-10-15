# 1.
while True:
    marks = int(input("Enter marks (0-100): "))
    if 0 <= marks <= 100:
        print("Accepted marks:", marks)
        break
    else:
        print("Invalid! Please enter between 0 and 100.")

# 2.
while True:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        print("Accepted number:", num)
        break
    else:
        print("Invalid! Must be greater than 0.")
# 3.
while True:
    age = int(input("Enter your age (0-120): "))
    if 0 <= age <= 120:
        print("Accepted age:", age)
        break
    else:
        print("Error! Age must be between 0 and 120.")

# 4.
while True:
    print("\nMenu:")
    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    
    choice = int(input("Enter choice (1-4): "))
    if choice in [1, 2, 3, 4]:
        print("You selected option:", choice)
        break
    else:
        print("Invalid choice! Try again.")

# 5.
while True:
    password = input("Enter password: ").strip()
    if len(password) >= 8:
        print("Password accepted!")
        break
    else:
        print("Password too short! Must be at least 8 characters.")

# 6.
while True:
    temp = int(input("Enter temperature (-20 to 45): "))
    if -20 <= temp <= 45:
        print("Accepted temperature:", temp)
        break
    else:
        print("Invalid! Must be between -20 and 45.")

# 7.
balance = 5000
while True:
    amount = int(input("Enter withdrawal amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdrawal successful! New balance:", balance)
        break
    else:
        print("Invalid amount! Try again.")

# 8.
while True:
    username = input("Enter username: ").strip()
    if len(username) >= 5 and " " not in username:
        print("Accepted username:", username)
        break
    else:
        print("Invalid username! Must be at least 5 characters, no spaces.")

# 9.
while True:
    num = int(input("Enter a positive integer divisible by 3 and 5: "))
    if num > 0 and num % 3 == 0 and num % 5 == 0:
        print("Accepted number:", num)
        break
    else:
        print("Invalid! Must be divisible by both 3 and 5.")

# 10.
secret_pin = 2468
attempts = 3

while attempts > 0:
    pin = int(input("Enter PIN: "))
    if pin == secret_pin:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print("Wrong PIN! Attempts left:", attempts)

if attempts == 0:
    print("Access denied!")

# 11.
while True:
    num = int(input("Enter number (10-50): "))
    if 10 <= num <= 50:
        print("Accepted:", num)
        print("Even" if num % 2 == 0 else "Odd")
        break
    else:
        print("Invalid! Must be between 10 and 50.")

# 12.
balance = 2000
while True:
    deposit = int(input("Enter deposit amount: "))
    if deposit > 0:
        balance += deposit
        print("Deposit successful! New balance:", balance)
        break
    else:
        print("Invalid! Deposit must be positive.")

# 13.
while True:
    num = int(input("Enter integer (1-100): "))
    if 1 <= num <= 100:
        print("Accepted number:", num)
        break
    else:
        print("Invalid! Must be between 1 and 100.")


# 14.
while True:
    marks = int(input("Enter marks (0-100): "))
    if 0 <= marks <= 100:
        if marks >= 75:
            print("Result: Distinction")
        elif marks >= 60:
            print("Result: First Class")
        elif marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
        break
    else:
        print("Invalid! Enter between 0 and 100.")


# 15.
while True:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if len(username) >= 5 and " " not in username and len(password) >= 8 and password != "":
        print("Login successful!")
        break
    else:
        print("Invalid! Username ≥5 chars, no spaces. Password ≥8 chars.")


# 16.
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator! Try again.")
        continue
    if operator == "/" and num2 == 0:
        print("Division by zero not allowed! Enter second number again.")
        continue
    
    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        print("Result:", num1 / num2)
    break

# 17.
balance = 10000
while True:
    print("\nBank Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("Balance:", balance)
    elif choice == 2:
        deposit = int(input("Enter deposit amount: "))
        if deposit > 0:
            balance += deposit
            print("Deposit successful! Balance:", balance)
        else:
            print("Invalid deposit!")
    elif choice == 3:
        withdraw = int(input("Enter withdrawal amount: "))
        if withdraw > 0 and withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful! Balance:", balance)
        else:
            print("Invalid withdrawal!")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")


# 18.
while True:
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))
    if 1 <= month <= 12 and 1 <= day <= 31:
        print("Accepted date: Month", month, "Day", day)
        break
    else:
        print("Invalid! Month 1-12, Day 1-31.")


# 19.
while True:
    quantity = int(input("Enter product quantity: "))
    if quantity > 0:
        break
    else:
        print("Invalid! Quantity must be positive.")

while True:
    price = float(input("Enter unit price: "))
    if price > 0:
        break
    else:
        print("Invalid! Price must be greater than 0.")

print("Total cost:", quantity * price)


# 20.
while True:
    count = int(input("How many numbers (1-20): "))
    if 1 <= count <= 20:
        break
    else:
        print("Invalid! Must be between 1 and 20.")

numbers = []
for i in range(count):
    while True:
        num = float(input(f"Enter number {i+1}: "))
        # Add range check if instructor specifies
        if True:  # replace with condition if needed
            numbers.append(num)
            break
        else:
            print("Invalid number! Try again.")

average = sum(numbers) / count
print("Average:", average)


# 21.
while True:
    password = input("Enter password: ")
    errors = []
    
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not any(c.isupper() for c in password):
        errors.append("At least one uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("At least one lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("At least one digit")
    if any(c.isspace() for c in password):
        errors.append("No whitespace allowed")
    
    if not errors:
        print("Password accepted!")
        break
    else:
        print("Invalid password! Issues:", ", ".join(errors))

# 22.
valid = False
while not valid:
    num = int(input("Enter integer (1-10): "))
    if 1 <= num <= 10:
        valid = True
        print("Accepted number:", num)
    else:
        print("Invalid! Try again.")


# 23.
scores = []
for i in range(3):
    while True:
        score = int(input(f"Enter score {i+1} (0-100): "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("Invalid! Must be between 0 and 100.")

total = sum(scores)
average = total / 3
print("Total:", total, "Average:", average)


# 24.
balance = 10000
while True:
    amount = int(input("Enter withdrawal amount: "))
    if amount > 0 and amount <= balance and amount % 100 == 0:
        balance -= amount
        print("Withdrawn:", amount, "Remaining balance:", balance)
        break
    else:
        print("Invalid! Must be positive, ≤ balance, and multiple of 100.")