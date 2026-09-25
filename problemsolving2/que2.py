failed_student = 0
excellent_student = 0
good_student = 0
pass_student = 0

for i in range(10):
    marks = int(input("enter your marks: "))
    if marks < 35:
        print("Fail")
        failed_student += 1
    elif 75 < marks <= 100:
        print("Excellent")
        excellent_student += 1
    elif 50 <= marks <= 74:
        print("Good")
        good_student += 1
    elif 35 <= marks <= 49:
        print("Pass")
        pass_student += 1
    else:
        print("Invalid marks entered")

print("Failed students:", failed_student)
print("Excellent students:", excellent_student)
print("Good students:", good_student)
print("Pass students:", pass_student)   
