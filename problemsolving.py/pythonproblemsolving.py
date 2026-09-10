num= int(input("enter a number"))

if num >0 :
    print("positive")
elif num <0 :
    print("negative")
else:
    print("equal to zero")


num= int(input("enter a number"))

if num >0 and num %2 == 0:
    print("positive even")
elif num >0 and num % 2 != 0:
    print("positive odd")
elif num <0 and num %2 == 0:
    print("negative even")
elif num <0 and num %2 != 0:
    print("negative odd")
else:
    print("zero")


num1= int(input("enter a number"))
num2= int(input("enter another number"))

if num1 > num2:
    print("num1 is greater")
elif num1 < num2:
    print("num2 is greater")
else:
    print("both are equal")


num1= int(input("enter a number"))
num2= int(input("enter second number"))
num3= int(input("enter third number"))

if num1<num2 and num1<num3 :
    smallest = num1
elif num2<num1 and num2<num3 :
    smallest = num2
else:
     smallest = num3

print("the smallest number is:",smallest)



num1= int(input("enter a number"))
num2= int(input("enter second number"))
num3= int(input("enter third number"))

if num1>num2 and num1>num3 :
    largest = num1
elif num2>num1 and num2>num3 :
    largest = num2
else:
     largest = num3

print("the largest number is:",largest)



num= int(input("enter a num"))

if num % 5 == 0 and num % 11 == 0:
    print("divisible by both 5 and 11")
elif num % 5 == 0:
    print("divisible by 5")
elif num % 11 == 0:
    print("divisible by 11")
else:
    print("divisible by neither")



num= int(input("enter a num"))

if num % 3 == 0 and num % 7 == 0:
    print("divisible by both 3 and 7")
elif num % 3 == 0:
    print("divisible by 3")
elif num % 7 == 0:
    print("divisible by 7")
else:
    print("divisible by neither")



marks= float(input("enter your marks"))

if marks < 0:
    print("invalid marks")
elif marks >100:
    print("invalid marks")
elif marks >=40:
    print("pass")
else:
    print("fail")



marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")



age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age < 18:
    print("Cannot vote")
else:
    print("Can vote")



year = int(input("enter any year"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")




ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase alphabet")
elif 'a' <= ch <= 'z':
    print("Lowercase alphabet")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")



ch = input("Enter a character: ")

if ch != 1 or not ch. isalpha():
    print("Invalid input")
elif ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")



cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit= selling_price - cost_price
    print("Profit =", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No profit and no loss")



cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if cost_price <= 0:
    print("Invalid cost price")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("Profit =", profit)
    print("Profit Percentage =", profit_percentage)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print("Loss =", loss)
    print("Loss Percentage =", loss_percentage)
else:
    print("No profit and no loss")



units = int(input("Enter total units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Total bill = ₹", bill)
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print("Total bill = ₹", bill)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("Total bill = ₹", bill)




first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("Cannot divide by zero")
    else:
        result = first_number / second_number
else:
    print("Invalid operator")
    result = None

if result is not None:
    if result.is_integer():
        print(int(result))
    else:
        print(result)



temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing")
elif temperature <= 15:
    print("Very Cold")
elif temperature <= 25:
    print("Cold")
elif temperature <= 35:
    print("Normal")
else:
    print("Hot")



number = int(input("Enter a number: "))

if number < 0:
    print("Number is negative")
elif 0 <= number <= 10:
    print("Number is between 0 and 10")
elif 11 <= number <= 50:
    print("Number is between 11 and 50")
elif 51 <= number <= 100:
    print("Number is between 51 and 100")
else:
    print("Number is above 100")



a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")



a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")



balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount")
elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal > balance:
    print("Insufficient balance")
elif balance - withdrawal < 500:
    print("At least ₹500 must remain in the account")
else:
    remaining_balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", remaining_balance)



username = input("Enter username: ")
password = input("Enter password: ")

if username != "admin":
    print("User not found")
elif password != "python123":
    print("Wrong password")
else:
    print("Login successful")



purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount < 500:
    discount_percent = 0
elif 500 <= purchase_amount <= 999:
    discount_percent = 5
elif 1000 <= purchase_amount <= 1999:
    discount_percent = 10
elif 2000 <= purchase_amount <= 4999:
    discount_percent = 15
else:
    discount_percent = 20

discount_amount = purchase_amount * (discount_percent / 100)
final_amount = purchase_amount - discount_amount

print("Original amount:", purchase_amount)
print("Discount percentage:", discount_percent, "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)


subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

if subject1 < 0 or subject1 > 100 or subject2 < 0 or subject2 > 100 or subject3 < 0 or subject3 > 100:
    print("Invalid marks")
elif subject1 < 35 or subject2 < 35 or subject3 < 35:
    print("Fail")
else:
    average = (subject1 + subject2 + subject3) / 3

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")



day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid date")
elif day < 1:
    print("Invalid date")
else:
    is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month == 2:
        if is_leap_year:
            max_day = 29
        else:
            max_day = 28
    else:
        max_day = 30

    if day <= max_day:
        print("Valid date")
    else:
        print("Invalid date")



hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Valid time")
else:
    print("Invalid time")



name1 = input("Enter name of person 1: ")
age1 = int(input("Enter age of person 1: "))
name2 = input("Enter name of person 2: ")
age2 = int(input("Enter age of person 2: "))
name3 = input("Enter name of person 3: ")
age3 = int(input("Enter age of person 3: "))

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")
elif age1 == age2 == age3:
    print(name1, name2, "and", name3, "have the same age")
elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")
elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")
elif age2 == age3 and age2 < age1:
    print(name2, "and", name3, "are the youngest")
else:
    print("All ages are equal")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num1 > num2:
        print(num1)
    else:
        print(num2)



