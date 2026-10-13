# Q1
# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")   

# OUTPUT:-
# 1 
# 2
# 3
# 4
# Finished 




# Q2
# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)


# OUTPUT:-
# s
# k 
# y
# l 



#Q3
# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2

# OUTPUT:-
# 2
# 4
# 6



# Q4
# limit=int(input("Enter any integer:-")) 
# for i in range(1,limit):
#       if i==7:
#             break
#       print(i, end=" ")  


# Q5
# str=input("Enter any string:-").strip().lower()
# for i in str:
#     if i=="e":
#         break
#     print(i) 


# Q6
# num=[10,20,-5,-8,17]
# for i in num:
#     if i<0:
#         break
#     print(i)  



# Q7
# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

# output:-
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# Q8
# sentence = input("Enter a sentence: ")
# target = input("Enter target word: ")

# words = sentence.split()

# for i in words:
#     if i == target:
#         print("Found")
#         break
# else:
#     print("Not found") 


# Q9
# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i) 
# OUTPUT:-
# 1
# 2
# 3
# 5
# 6


#Q10 
# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")
# OUTPUT:-
# d
# c 
# t 
# n


# Q11
n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# OUTPUT:-
# 1
# 2
# 4
# 5

# Q12 
# n=int(input("Enter any  integer:-"))
# for i in range(n):
#     if i%3==0:
#         continue
#     print(i)  



# Q13
# str=input("Enter any string:-")
# for i in str:
#     if i=="a":
#         continue
#     print(i) 



# Q14
# num=[25, 40, 75, 32, 90]
# for i in num:
#     if i<35:
#         continue
#     print(i)


# Q15
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

# OUTPUT:-
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4


# Q16
# n = 0

# while n < 5:
#     n+=1
#     if n == 3:
        
#         continue
    
#     print(n)


# Q17
# str=input("Enter any string:-").strip().lower()
# count=0
# for i in str:
#     if i in "aeiou":
#        count+=1
#        continue
# print(count)  


# Q18
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")

# OUTPUT:-
# 1
# 2
# 3
# Done 


# Q19
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

# OUTPUT:-
# 1
# 3
# 4
# Completed 



# Q20
# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")


# OUTPUT:-
# 1
# 2
# Outside loop 


# Q21
# for item in []:
#     print("Inside")
# else:
#     print("Else block")

# OUTPUT:-
# Else block 



# Q22

# num=[12,14,16,18,20]

# for i in num:
#     if i==12:
#         print("Found")
#         break
# else:
#     print("Not found")  


# Q23
# str=input("Enter any string:-")
# for i in str:
#     if i=="a":
#         print("Character exists")
#         break
# else:
#     print("Character not found")


# Q24


# Q25
# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# OUTPUT:- All are even


# Q26
# case 1 
# for x in range(3):
#     continue
# else:
#     print("A")   OUTPUT:- A


# case 2
# for x in range(3):
#     break
# else:
#     print("B")  OUTPUT:- B


# case 3
# for x in range(0):
#     print(x)
# else:
#     print("C")

# OUTPUT:- 
# C


# Q27
# str = "markram"
# for ch in str:
#     if str.count(ch) > 1:
#         print(ch)
#         break
# else:
#     print("not repeated")


# Q28

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

# OUTPUT:-
# 1
# 2
# 3

# Q29
# x = 10

# if x > 5:
#     pass

# print("Finished")

# OUTPUT:-
# Finished


# Q30

# for letter in "cat":
#     pass

# print("Loop ended")

# OUTPUT:-
# LOOP ENDED


# Q31

