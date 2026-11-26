# 1
# def show(n):
#     if n==0:
#         print("End")
#         return
#     print("Start",n)
#     show(n-1)
#     print("Back",n)
# show(2)

# def show(n):
#     if n == 0:
#         print("Stop")
#         return

#     print(n)
#     show(n - 1)
#     print(n)

# show(2)


# 2
# def total(n):
#     if n == 0:
#         return 0

#     return n + total(n - 1)
# print(total(2))



# 3
# def count(n):
#     if n == 4:
#         print("End")
#         return
#     print("Start",n)
#     count(n + 1)
#     print("Back",n)
# count(2)


# 4
# def answer(n):
#     if n == 0:
#         return n + answer(n - 1)
#     print(n)
# print(answer(3))



# 5
# def num(n):
#     if n==0:
#         print("Done!")
#         return
#     print(n)
#     num(n-1)
# num(3)



# 6
# def num(n):
#     if n==5:
#         return
#     print(n)
#     num(n+1)
# num(1)


# 7
# add=0
# def addition(n):
#     global add
#     add +=n
#     if (n==5):
#         return add
#     return addition(n+1)
# print(addition(1))



# 8
# add=1
# def addition(n):
#     global add
#     add *=n
#     if (n==5):
#         return add
#     return addition(n+1)
# print(addition(1))



# 9
# def digit_sum(n):
#     if n == 0:
#         return 0
#     return (n % 10) + digit_sum(n // 10)
# print(digit_sum(583)) 
# print(digit_sum(7))   
# print(digit_sum(0))  
     


# 10
# def power(n,m):
#     if n==0:
#         return 1
#     print(n**m)
# power(2,3)



# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
# print(power(3, 3))



# 11
# def digit(n):
#     if n < 10:
#         return 1
#     else:
#         return 1 + digit(n // 10)
# print(digit(12347))



# 12
# def reverse(text):
#   if len(text) <= 1:
#     return text
#   return reverse(text[1:]) + text[0]
# print(reverse("cat"))

# def reverse(text):
#   if text=="":
#     return ""
#   return text[-1]+reverse(text[:-1])
# print(reverse("cat"))



# 13
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))



# 15
# def mystery(n):
#     if n <= 1:
#         return n

#     return mystery(n - 1) + mystery(n - 2)
# print(mystery(7))
# print(mystery(2))
# print(mystery(1))



# 16
# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)
# print(factorial(4))
# print(factorial(0))



# 17
# def stop_at_zero(n):
#     if n == 0:
#         return 8

#     return stop_at_zero(n - 1)
# print(stop_at_zero(5))



# 18
