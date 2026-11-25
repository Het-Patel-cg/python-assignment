# que 1
# def city():
#     name = "rajkot"
#     print(name)

# city()


# que 2
# school = "abc school"

# def show_name():
#     print(school)

# show_name()


# que 3
# if True:
#     message = "Hello from inside the if block"

# print(message)


# que 4
# for number in range(1, 4):
#     last_number = number

# print(last_number)




# que 6
# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)

# output :- 200
          # 100


# que 7
# clicks = 0

# def click():
#     global clicks
#     clicks += 1

# click()
# print(clicks)  # 1

# que 8
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# ans :> f you want to print the global name and then change it locally so use a different local variable


# que 9
# def outer():
#     message = "Hello from the enclosing function"

#     def inner():
#         print(message)

#     inner()

# outer()


# que 10
# def make_list():
#     return [1, 2, 3]

# numbers = make_list()
# numbers.append(4)

# print(numbers)


# que 11
# def make_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter


# next_number = make_counter()

# print(next_number())  # 1
# print(next_number())  # 2
# print(next_number())  # 3


# que 12
# output = 3
        #  2
        #  1

# que 14
# def make_greeting(name):
#     def greet():
#         return f"Hello, {name}!"
#     return greet


# say_hello = make_greeting("Asha")
# print(say_hello())
