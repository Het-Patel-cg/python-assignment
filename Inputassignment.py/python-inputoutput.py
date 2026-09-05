name= input("Enter your name: ")
city= input("Your city is: ")
username= input("Enter your username: ")
age= input("Enter your age: ")
print("name", name)
print("city", city)
print("username", username)
print("age", age)

value= input("Enter your salary: ")
print("Your salary is: ", value)
print("Type of your salary is: ", type(value))

first_name= input("Enter your first name: ")
last_name= input("Enter your last name: ")
print("Your full name is: ", first_name + " " + last_name)


name=input("Enter your name: ")
city=input("Enter your city: ")
college=input("Enter your college name: ")

print("My name is: ", name)
print("My city is: ", city)
print("My college is: ", college)


name, city, college = input("Enter your name, city and college name: ").split()

print("Name:",name)
print("City:",city)
print("College:",college)


name, city, college = input("Enter name, city, and college: ").split()



word1, word2, word3 = input("Enter three words: ").split()

print("first word:", word1)
print("second word:", word2)
print("third word:", word3)

s="25"
number = int(s)
print(number)

s="25.5"
number = float(s)
print(number)

s=100
number = str(s)
print(number)

num = int(input("Enter a integer: "))

print("You entered:", num)
print("Type after conversion:", type(num))



num = float(input("Enter a floating-point number: "))

print("You entered:", num)
print("Type after conversion:", type(num))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

name="Rahul"
age=20

print(f"My name is {name} and I am {age} years old. I live in {city}.")


a=10
b=20

print(f"The sum of {a} and {b} is {a + b}.")

name=input("Enter your name: ")
age=int(input("Enter your age: "))


print(f"My name is {name} and I am {age} years old.")


price=float(input("Enter the price of the item: "))
print(f"The price of the item is ${price:}")


price = 22
print(f"{price:.2f}")
productname=("Tea ")
price=("20.00")
quantity=("4")

print(f"Enter name {productname}, price {price}, quantity {quantity}")


print("A", "B", "C")


print("2026", "08", "19", sep="-")


print("Hello", end=" ")
print("World!")


integer1=int(input("Enter first integer: "))
integer2=int(input("Enter second integer: "))

print(f"The sum of {integer1} and {integer2} is {integer1 + integer2}.")


price=int(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item: "))
total_cost=price*quantity

print(f"The total cost of {quantity} items at ${price} each is ${total_cost}.")


name=input("Enter your name: ")
age=int(input("Enter your age: "))
marks=float(input("Enter your marks: "))

print(f"Name: {name}, Age: {age}, Marks: {marks:.2f}")



studentname=input("Enter student name: ")
studentage=int(input("Enter student age: "))
studentheight=float(input("Enter student height:"))
city=input("Enter student city: ")


print(f"Student Name: {studentname}, Age: {studentage}, Height: {studentheight:.2f}, City: {city}")
