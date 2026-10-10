# 1.

# user = int(input("Enter a number: "))
# match user:
#     case 1:
#         print("you choosed pizza")
#     case 2:
#         print("you choosed burger")
#     case 3:
#         print("you choosed pasta")
#     case 4:
#         print("you choosed sandwich")
#     case _:
#         print("invalid menu choice")


# 2.

# setting_menu = int(input("Enter a number: "))
# match setting_menu:
#     case 1:
#         print("you choosed wifi settings")
#     case 2:
#         print("you choosed bluetooth settings")
#     case 3:
#         print("you choosed mobile data settings")
#     case 4:
#         print("you choosed airplane mode settings")
#     case 5:
#         print("exit")
#     case _:
#         print("invalid setting choice")


# 3.

# atm_menu = int(input("Enter a number: "))
# match atm_menu:
#     case 1:
#         print("you choosed check balance")
#     case 2:
#         print("you choosed withdraw")
#     case 3:
#         print("you choosed deposit")
#     case 4:
#         print("you choosed changed pin")
#     case 5:
#         print("exit")
#     case _:
#         print("invalid atm choice")


# 4.

# colour = input("enter colour name: ")
# match colour:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("wait")
#     case "green":
#         print("go")
#     case _:
#         print("invalid_signal")


# 5.

# student_portal = int(input("enter any integer"))
# match student_portal:
#     case 1:
#         print("view profile")
#     case 2:
#         print("view courses")
#     case 3:
#         print("view marks")
#     case 4:
#         print("view attendance")
#     case 5:
#         print("logout")
#     case _:
#         print("exit")


# 6.

# shopping_menu = int(input("enter a integer: "))
# match shopping_menu:
#     case 1:
#         print("electronics")
#     case 2:
#         print("clothing")
#     case 3:
#         print("books")
#     case 4:
#         print("grocery")
#     case _:
#         print("exit")


# 7.

# banking_service = int(input("enter a integer: "))
# match banking_service:
#     case 1:
#         print("account balance")
#     case 2:
#         print("mini statement")
#     case 3:
#         print("fund transfer")
#     case 4:
#         print("bill payment")
#     case 5:
#         print("customer service")
#     case _:
#         print("close chat")


# 8.

# movie_ticket = int(input("enter a integer: "))
# match movie_ticket:
#     case 1:
#         print("morning show selected")
#     case 2:
#         print("afternoon show selected")
#     case 3:
#         print("evening show selected")
#     case 4:
#         print("night show selected")
#     case _:
#         print("close booking")


# 9.

# weather = input("enter any weather: ")
# match weather:
#     case "sunny":
#         print("wear sunglasses")
#     case "rainy":
#         print("carry an umbrella")
#     case "cloudy":
#         print("weather may change")
#     case "snowy":
#         print("wear warm clothes")
#     case _:
#         print("invalid weather")


# 10.

# payment_method = str(input("select payment method"))
# match payment_method:
#     case "upi":
#         print("upi selected")
#     case "card":
#         print("card selected")
#     case "cash":
#         print("cash selected")
#     case "wallet":
#         print("wallet selected")
#     case _:
#         print("error")


# 11.

# extension = str(input("select an extension"))
# match extension:
#     case "pdf":
#         print("document")
#     case "jpg":
#         print("image")
#     case "png":
#         print("image")
#     case "mp3":
#         print("audio")
#     case "mp4":
#         print("video")
#     case _:
#         ("unknown file type")


# 12.

# user_role = str(input("enter accesser"))
# match user_role:
#     case "student":
#         print("student dashboard")
#     case "admin":
#         print("full access")
#     case "teacher":
#         print("teacher dashboard")
#     case "guest":
#         print("limited access")
#     case _:
#         print("invalid role")


# 13.

# day = int(input("enter a number between 1 to 7:"))
# match day:
#     case 1|2|3|4|5:
#         print("weekday")
#     case 6|7:
#         print("weekend")
#     case _:
#         print("invalid input")


# 14.

# print("1. low\n 2. medium\n 3.high\n 4. critical")
# customer_support = int(input("enter a integer: "))
# match customer_support:
#      case 1|2:
#          print("low urgency")
#      case 3|4:
#          print("high urgency")
#      case _:
#          print("invalid input")


# 15.

# print("1. bronze\n 2. silver\n. 3. gold\n. 4. platinum")
# store_discount = int(input("enter a integer"))
# match store_discount:
#     case 1|2:
#         print("basic membership")
#     case 3|4:
#         print("premium membership")
#     case _:
#         print("inappropriate category")


# 16.

# user_type = int(input("Enter user type: "))
# match user_type:
#     case 1:
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Opening Student Courses")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case _:
#                 print("Invalid option")
#     case 2:
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Entering Teacher Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid user type")


# 17.

# print("1 → Savings\n2 → Current")
# account_type = int(input("Enter account type: "))
# match account_type:
#     case 1:
#         print("Savings Account")
#         print("1 → Check Balance\n2 → Deposit\n3 → Withdraw")
#         operation = int(input("Enter operation: "))
#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid operation")
#     case 2:
#         print("Current Account")
#         print("1 → Check Balance\n2 → Deposit\n3 → Withdraw")
#         operation = int(input("Enter operation: "))
#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid operation")
#     case _:
#         print("Invalid account type")


# 18.

# print("1 → Electronics\n2 → Clothing")
# category = int(input("Enter category: "))
# match category:
#     case 1:
#         print("1 → Mobile\n2 → Laptop\n3 → Headphones")
#         product = int(input("Enter product: "))
#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid product")
#     case 2:
#         print("1 → Shirt\n2 → Jeans\n3 → Shoes")
#         product = int(input("Enter product: "))
#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid product")
#     case _:
#         print("Invalid category")


# 19.

# print("1 → Vegetarian\n2 → Non-Vegetarian")
# category = int(input("Enter category: "))
# match category:
#     case 1:
#         print("1 → Paneer\n2 → Dal\n3 → Veg Biryani")
#         food = int(input("Enter food: "))
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid food")
#     case 2:
#         print("1 → Chicken Biryani\n2 → Chicken Curry\n3 → Fish Fry")
#         food = int(input("Enter food: "))
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid food")
#     case _:
#         print("Invalid category")


# 20.

# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# operator = input("Enter operator: ")

# match operator:
#     case "+":
#         result = first_number + second_number
#     case "-":
#         result = first_number - second_number
#     case "*":
#         result = first_number * second_number
#     case "/":
#         if second_number == 0:
#             print("Cannot divide by zero")
#         else:
#             result = first_number / second_number
#     case _:
#         print("Invalid operator")

# if operator in {"+", "-", "*"} or (operator == "/" and second_number != 0):
#     print(f"Result = {result:g}")


# 21.

# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         temperature = float(input("Enter temperature: "))
#         fahrenheit = (temperature * 9 / 5) + 32
#         print(f"Temperature = {fahrenheit} F")
#     case 2:
#         temperature = float(input("Enter temperature: "))
#         celsius = (temperature - 32) * 5 / 9
#         print(f"Temperature = {celsius} C")
#     case _:
#         print("Invalid choice")


# 22.

# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         value = float(input("Enter value: "))
#         print(f"{value * 1000:g} meters")
#     case 2:
#         value = float(input("Enter value: "))
#         print(f"{value / 1000:g} kilometers")
#     case 3:
#         value = float(input("Enter value: "))
#         print(f"{value * 1000:g} grams")
#     case 4:
#         value = float(input("Enter value: "))
#         print(f"{value / 1000:g} kilograms")
#     case _:
#         print("Invalid choice")


# 23.

# print("1 → Savings\n2 → Current")
# account_type = int(input("Enter account type: "))
# match account_type:
#     case 1:
#         print("Savings Account")
#         amount = float(input("Enter amount: "))
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")
#     case 2:
#         print("Current Account")
#         amount = float(input("Enter amount: "))
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")
#     case _:
#         print("Invalid account type")


# 24.

# print("1 → Start Exam\n2 → View Result\n3 → Exit")
# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         age = int(input("Enter age: "))
#         if age >= 18:
#             print("You can start the exam")
#         else:
#             print("You cannot start the exam")
#     case 2:
#         print("Viewing Result")
#     case 3:
#         print("Exiting Portal")
#     case _:
#         print("Invalid choice")


# 25.

# print("1 → Regular\n2 → Premium\n3 → VIP")
# ticket_type = int(input("Enter ticket type: "))
# match ticket_type:
#     case 1:
#         ticket_name = "Regular"
#     case 2:
#         ticket_name = "Premium"
#     case 3:
#         ticket_name = "VIP"
#     case _:
#         ticket_name = "Invalid"
#
# if ticket_name == "Invalid":
#     print("Invalid ticket type")
# else:
#     age = int(input("Enter age: "))
#     if age < 5:
#         print("Free Entry")
#     else:
#         print(f"{ticket_name} Ticket Selected")


# 26.

# print("1 → Light\n2 → Fan\n3 → AC\n4 → TV")
# device = int(input("Enter device: "))
# match device:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Invalid device")


# 27.

# print(
#     "1 → General Medicine\n2 → Cardiology\n3 → Orthopedics\n"
#     "4 → Pediatrics\n5 → Emergency"
# )
# department = int(input("Enter department: "))
# match department:
#     case 1:
#         print("General Medicine")
#     case 2:
#         print("Cardiology")
#     case 3:
#         print("Orthopedics")
#     case 4:
#         print("Pediatrics")
#     case 5:
#         print("Emergency")
#     case _:
#         print("Invalid Department")


# 28.

# print("1 → Book Ticket\n2 → Cancel Ticket\n3 → Check PNR\n"
#       "4 → Train Schedule\n5 → Exit")
# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         print("Booking Ticket")
#     case 2:
#         print("Cancelling Ticket")
#     case 3:
#         print("Checking PNR")
#     case 4:
#         print("Showing Train Schedule")
#     case 5:
#         print("Exiting")
#     case _:
#         print("Invalid choice")


# 29.

# print("1 → Search Book\n2 → Issue Book\n3 → Return Book\n"
#       "4 → View Issued Books\n5 → Exit")
# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         print("Searching Book")
#     case 2:
#         print("Issuing Book")
#     case 3:
#         print("Returning Book")
#     case 4:
#         print("Viewing Issued Books")
#     case 5:
#         print("Exiting Library")
#     case _:
#         print("Invalid choice")


# 30.

# status = input("Enter status: ")
# match status:
#     case "placed":
#         print("Your order has been placed")
#     case "confirmed":
#         print("Your order is confirmed")
#     case "preparing":
#         print("Your order is being prepared")
#     case "out_for_delivery":
#         print("Your order is on the way")
#     case "delivered":
#         print("Your order has been delivered")
#     case "cancelled":
#         print("Your order has been cancelled")
#     case _:
#         print("Invalid order status")


# 31.

# print("1 → Personal Banking\n2 → Business Banking")
# banking_type = int(input("Enter banking type: "))
# match banking_type:
#     case 1:
#         print("1 → Balance\n2 → Transfer\n3 → Loan")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Personal Balance Selected")
#             case 2:
#                 print("Personal Transfer Selected")
#             case 3:
#                 print("Personal Loan Selected")
#             case _:
#                 print("Invalid option")
#     case 2:
#         print("1 → Balance\n2 → Payroll\n3 → Business Loan")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Business Balance Selected")
#             case 2:
#                 print("Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid banking type")


# 32.

# print("1 → Student\n2 → Teacher\n3 → Parent")
# role = int(input("Enter role: "))
# match role:
#     case 1:
#         print("1 → Marks\n2 → Attendance\n3 → Homework")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Student Marks")
#             case 2:
#                 print("Student Attendance")
#             case 3:
#                 print("Student Homework")
#             case _:
#                 print("Invalid option")
#     case 2:
#         print("1 → Enter Marks\n2 → Attendance\n3 → Assign Homework")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Entering Marks")
#             case 2:
#                 print("Teacher Attendance")
#             case 3:
#                 print("Assigning Homework")
#             case _:
#                 print("Invalid option")
#     case 3:
#         print("1 → Child Marks\n2 → Child Attendance\n3 → Contact Teacher")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Child Marks")
#             case 2:
#                 print("Child Attendance")
#             case 3:
#                 print("Contacting Teacher")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid role")


# 33.

# print("1 → Flight\n2 → Train\n3 → Bus")
# transport = int(input("Select transport: "))
# match transport:
#     case 1:
#         print("1 → Economy\n2 → Business")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Flight Economy Selected")
#             case 2:
#                 print("Flight Business Selected")
#             case _:
#                 print("Invalid option")
#     case 2:
#         print("1 → Sleeper\n2 → AC")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Train Sleeper Selected")
#             case 2:
#                 print("Train AC Selected")
#             case _:
#                 print("Invalid option")
#     case 3:
#         print("1 → Ordinary\n2 → Volvo")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Bus Ordinary Selected")
#             case 2:
#                 print("Bus Volvo Selected")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid transport")


# 34.

# print("1 → Start Game\n2 → Load Game\n3 → Settings\n4 → Exit")
# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         print("Starting Game")
#     case 2:
#         print("Loading Game")
#     case 3:
#         print("1 → Sound\n2 → Graphics\n3 → Controls")
#         setting = int(input("Enter setting: "))
#         match setting:
#             case 1:
#                 print("Sound Settings")
#             case 2:
#                 print("Graphics Settings")
#             case 3:
#                 print("Control Settings")
#             case _:
#                 print("Invalid setting")
#     case 4:
#         print("Exiting Game")
#     case _:
#         print("Invalid choice")


# 35.

# print("1 → Starters\n2 → Main Course\n3 → Desserts\n4 → Drinks")
# category = int(input("Enter category: "))
# match category:
#     case 1:
#         print("1 → Soup\n2 → Spring Roll\n3 → Garlic Bread")
#         item = int(input("Enter item: "))
#         match item:
#             case 1:
#                 print("Soup Selected")
#             case 2:
#                 print("Spring Roll Selected")
#             case 3:
#                 print("Garlic Bread Selected")
#             case _:
#                 print("Invalid item")
#     case 2:
#         print("1 → Pizza\n2 → Pasta\n3 → Biryani")
#         item = int(input("Enter item: "))
#         match item:
#             case 1:
#                 print("Pizza Selected")
#             case 2:
#                 print("Pasta Selected")
#             case 3:
#                 print("Biryani Selected")
#             case _:
#                 print("Invalid item")
#     case 3:
#         print("1 → Ice Cream\n2 → Cake\n3 → Gulab Jamun")
#         item = int(input("Enter item: "))
#         match item:
#             case 1:
#                 print("Ice Cream Selected")
#             case 2:
#                 print("Cake Selected")
#             case 3:
#                 print("Gulab Jamun Selected")
#             case _:
#                 print("Invalid item")
#     case 4:
#         print("1 → Coffee\n2 → Tea\n3 → Juice")
#         item = int(input("Enter item: "))
#         match item:
#             case 1:
#                 print("Coffee Selected")
#             case 2:
#                 print("Tea Selected")
#             case 3:
#                 print("Juice Selected")
#             case _:
#                 print("Invalid item")
#     case _:
#         print("Invalid category")


# 36.

# print("1 → UPI\n2 → Card\n3 → Wallet")
# payment_type = int(input("Enter payment type: "))
# match payment_type:
#     case 1:
#         print("1 → Scan QR\n2 → Enter UPI ID")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Scan QR Selected")
#             case 2:
#                 print("Enter UPI ID Selected")
#             case _:
#                 print("Invalid option")
#     case 2:
#         print("1 → Credit Card\n2 → Debit Card")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Credit Card Selected")
#             case 2:
#                 print("Debit Card Selected")
#             case _:
#                 print("Invalid option")
#     case 3:
#         print("1 → Add Money\n2 → Pay Using Wallet")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Add Money Selected")
#             case 2:
#                 print("Pay Using Wallet Selected")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid payment type")


# 37.

# print("1 → Programming\n2 → Mathematics\n3 → Communication")
# subject = int(input("Enter subject: "))
# match subject:
#     case 1:
#         print("1 → Python\n2 → Java\n3 → C++")
#         course = int(input("Enter course: "))
#         match course:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid course")
#     case 2:
#         print("1 → Algebra\n2 → Calculus\n3 → Statistics")
#         course = int(input("Enter course: "))
#         match course:
#             case 1:
#                 print("Algebra Selected")
#             case 2:
#                 print("Calculus Selected")
#             case 3:
#                 print("Statistics Selected")
#             case _:
#                 print("Invalid course")
#     case 3:
#         print("1 → English\n2 → Presentation\n3 → Interview Skills")
#         course = int(input("Enter course: "))
#         match course:
#             case 1:
#                 print("English Selected")
#             case 2:
#                 print("Presentation Selected")
#             case 3:
#                 print("Interview Skills Selected")
#             case _:
#                 print("Invalid course")
#     case _:
#         print("Invalid subject")


# 38.

# print("1 → Engine\n2 → Lights\n3 → Music\n4 → Navigation")
# dashboard_option = int(input("Enter option: "))
# match dashboard_option:
#     case 1:
#         print("1 → Start\n2 → Stop")
#         option = int(input("Enter engine option: "))
#         match option:
#             case 1:
#                 print("Engine Started")
#             case 2:
#                 print("Engine Stopped")
#             case _:
#                 print("Invalid engine option")
#     case 2:
#         print("1 → Headlights\n2 → Indicators\n3 → Hazard Lights")
#         option = int(input("Enter lights option: "))
#         match option:
#             case 1:
#                 print("Headlights Selected")
#             case 2:
#                 print("Indicators Selected")
#             case 3:
#                 print("Hazard Lights Selected")
#             case _:
#                 print("Invalid lights option")
#     case 3:
#         print("1 → Play\n2 → Pause\n3 → Next\n4 → Previous")
#         option = int(input("Enter music option: "))
#         match option:
#             case 1:
#                 print("Music Playing")
#             case 2:
#                 print("Music Paused")
#             case 3:
#                 print("Playing Next Track")
#             case 4:
#                 print("Playing Previous Track")
#             case _:
#                 print("Invalid music option")
#     case 4:
#         print("1 → Start Navigation\n2 → Stop Navigation")
#         option = int(input("Enter navigation option: "))
#         match option:
#             case 1:
#                 print("Navigation Started")
#             case 2:
#                 print("Navigation Stopped")
#             case _:
#                 print("Invalid navigation option")
#     case _:
#         print("Invalid dashboard option")


# 39.

# print("1 → Employee\n2 → Manager")
# role = int(input("Enter role: "))
# match role:
#     case 1:
#         print("1 → View Profile\n2 → Apply Leave\n3 → View Salary")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Viewing Profile")
#             case 2:
#                 leave_days = int(input("Enter number of leave days: "))
#                 if leave_days > 0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")
#             case 3:
#                 print("Viewing Salary")
#             case _:
#                 print("Invalid option")
#     case 2:
#         print("1 → View Team\n2 → Approve Leave\n3 → View Reports")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Viewing Team")
#             case 2:
#                 print("Approving Leave")
#             case 3:
#                 print("Viewing Reports")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid role")


# 40.

# print("1 → Student\n2 → Teacher\n3 → Administration")
# role = int(input("Enter role: "))
# match role:
#     case 1:
#         print("1 → Profile\n2 → Marks\n3 → Attendance\n4 → Courses")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Opening Student Profile")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case 4:
#                 print("Opening Student Courses")
#             case _:
#                 print("Invalid option")
#     case 2:
#         print("1 → Students\n2 → Enter Marks\n3 → Attendance\n4 → Courses")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Entering Teacher Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case 4:
#                 print("Opening Teacher Courses")
#             case _:
#                 print("Invalid option")
#     case 3:
#         print("1 → Fees\n2 → Admissions\n3 → Notices\n4 → Departments")
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print("Opening Administration Fees")
#             case 2:
#                 print("Opening Administration Admissions")
#             case 3:
#                 print("Opening Administration Notices")
#             case 4:
#                 print("Opening Administration Departments")
#             case _:
#                 print("Invalid option")
#     case _:
#         print("Invalid role")
