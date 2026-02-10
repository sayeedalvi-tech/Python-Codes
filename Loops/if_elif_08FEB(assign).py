# 1.Write a program to assign grades based on
# student marks using the following conditions:
# ≥ 90 → A Grade
# ≥ 75 → B Grade
# ≥ 60 → C Grade
# ≥ 35 → Pass
# Else → Fail
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# 2.Write a program to validate login credentials
# and display appropriate messages.
user ="admin"
pwd ="1234"
username=input("Enter your username: ")
password=input("Enter your password: ")
if username=="admin" and password=="1234":
    print("Welcome")
elif username=="admin" and password!="1234":
    print("Invalid password")
elif username!="admin" and password=="1234":
    print("Invalid username")
elif username!="admin" and password!="1234":
    print("Invalid credentials")
else:
    print("Error")


# 3.Write a program to check whether a given number is
# even, odd, or zero.
num = int(input("Enter a number: "))
if num == 0:
    print("Number is zero")
elif num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 4.Write a program to check whether a number is
# single-digit, double-digit, or more
num = int(input("Enter a number: "))
if 0 <= num < 10 or -10 < num <= -1:
    print("The number is single-digit number")
elif 10 <= num < 100 or -100 < num <= 10:
    print("The number is double-digit number")
else:
    print("The number has more digits")


# 5.Write a program to check whether a number is divisible
# by 3, 5, or both.
# num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif num % 3==0:
    print("The number is divisible by 3")
elif num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 3,5 or both")


# 6.      ATM Withdrawal
# Write a program to check withdrawal status:
# Balance < amount → Insufficient balance
# Amount > 20,000 → Daily limit exceeded
# Otherwise → Transaction successful
balance = int(input("Enter balance: "))
amount = int(input("Enter amount: "))
if amount > balance:
    print("Insufficient balance")
elif amount > 20000:
    print("Daily limit exceeded")
else:
    print("Transaction successful")


# 7.     Mobile Battery Status
# Display battery condition based on percentage:
# 80–100 → Fully Charged
# 50–79 → Good
# 20–49 → Low
# < 20 → Critical
n = int(input("Enter battery percentage:"))
if 80 <= n <= 100:
    print("Fully Charged")
elif 50 <= n <= 79:
    print("Good")
elif 20 <= n <= 49:
    print("Low")
else:
    print("Critical")


# 8.     Traffic Signal System
# Display message based on signal color:
# Red → Stop
# Yellow → Ready
# Green → Go
# Else → Invalid signal
signal = input("Enter signal:")
if signal=="Red" or signal=="red" or signal=="RED":
    print("Stop")
elif signal=="Yellow" or signal=="yellow" or signal=="YELLOW":
    print("Ready")
elif signal=="Green" or signal=="green" or signal=="GREEN":
    print("Go")
else:
    print("Invalid Signal")


# 9.     Movie Ticket Pricing
# Ticket price based on age:
# Below 12 → ₹100
# 12–59 → ₹200
# 60 and above → ₹150
age = int(input("Enter your age: "))
if age < 12:
    print("Ticket price is 100")
elif 12 <= age <= 59:
    print("Ticket price is 200")
elif age > 59:
    print("Ticket price is 150")


# 10.    Student Attendance Eligibility
# Attendance percentage:
# ≥ 75 → Eligible
# 60–74 → Conditionally eligible
# < 60 → Not eligible
attendance = eval(input("Enter your attendance: "))
if attendance >=75:
    print("Eligible")
elif 60 <= attendance <= 74:
    print("Conditionally Eligible")
elif attendance < 60:
    print("Not Eligible")


# 11.    Weather Advisory System
# Based on temperature:
# ≥ 40 → Heat Alert
# 30–39 → Hot
# 20–29 → Normal
# < 20 → Cold
temp = int(input("Enter temperature: "))
if temp >= 40:
    print("Heat Alert")
elif 30 <= temp <=39:
    print("Hot")
elif 20 <= temp <=29:
    print("Normal")
elif temp < 20:
    print("Cold")


# 12.   Loan Approval System
# Conditions: (take salary and Cibil userinput)
# Salary ≥ 50,000 & CIBIL ≥ 750 → Approved
# Salary ≥ 30,000 & CIBIL ≥ 650 → Review
# Else → Rejected
sal = int(input("Enter your salary: "))
cibil = int(input("Enter your cibil: "))
if sal >= 50000 and cibil >= 750:
    print("Loan approved")
elif sal >= 30000 and cibil >= 650:
    print("Review")
else:
    print("Rejected")


# 13.  Restaurant Order System
# Choice:
# 1 → Veg Meal
# 2 → Non-Veg Meal
# 3 → Snacks
# Else → Invalid choice
ch = int(input("Enter your choice: "))
if ch == 1:
    print("Veg Meal")
elif ch == 2:
    print("Non-Veg Meal")
elif ch == 3:
    print("Snacks")
else:
    print("Invalid Choice")


# 14.   Internet Data Usage Alert
# Data used (GB):
# < 50 → Normal usage
# 50–80 → Warning
# 80 → Limit exceeded
data = int(input("Enter data used in GB:"))
if data < 50:
    print("Normal usage")
elif 50 <= data <= 80:
    print("Warning")
elif data > 80:
    print("Limit Exceeded")


# 15.  Write a program to calculate tip percentage based on service rating:
# Excellent → 20%
# Good → 15%
# Average → 10%
# Poor → No tip
rating = input("Enter rating: ")
if rating == "Excellent" or rating == "excellent":
    print("Tip percentage is 20%")
elif rating == "Good" or rating == "good":
    print("Tip percentage is 15%")
elif rating == "Average" or rating == "average":
    print("Tip percentage is 10%")
elif rating == "poor" or rating == "poor":
    print("No tip")
else:
    print("Invalid rating")


# 16.  Railway Ticket Category
# Write a program to decide ticket category based on age:
# Below 5 → Free
# 5 to 17 → Half Ticket
# 18 to 59 → Full Ticket
# 60 and above → Senior Citizen Ticket

age=int(input("Enter Age:"))
if age<5:
    print("Free Ticktet")
elif 5>=age>=17:
    print("Half Ticket")
elif 18>=age>=59:
    print("Full Ticket")
else:
    print("Senior citizen ticket")


# 17.  Internet Speed Status
# Write a program to display internet speed status based on Mbps:
# ≥ 100 → Super Fast
# 50–99 → Fast
# 10–49 → Moderate
# # < 10 → Slow
speed = int(input("Enter internet speed: "))
if speed >= 100:
    print("Super Fast")
elif 50 <= speed <= 99:
    print("Fast")
elif 10 <= speed <= 49:
    print("Moderate")
elif speed < 10:
    print("Slow")


# 18. School Fee Fine System
# Write a program to calculate late fee fine based on days delayed:
# ≤ 5 days → No fine
# 6–10 days → ₹50
# 11–20 days → ₹100
# More than 20 days → ₹200
days = int(input("Enter the number of days delayed: "))
if days <= 5:
    print("No fine")
elif 6 <= days <= 10:
    print("Fine of Rs.50")
elif 11 <= days <= 20:
    print("Fine of Rs.100")
elif days > 20:
    print("Fine of Rs.200")


# 19.Employee Shift Allocation
# Write a program to allocate employee shift based on login time (24-hour format):
# 6–13 → Morning Shift
# 14–21 → Evening Shift
# Else → Night Shift
time = int(input("Enter login time:"))
if 6 <= time <=13:
    print("Morning Shift")
elif 14 <= time <= 21:
    print("Evening Shift")
else:
    print("Night Shift")


# 20.Online Food Delivery Charges
# Write a program to calculate delivery charges based on order amount:
# Order amount ≥ 500 → Free Delivery
# Order amount 300–499 → ₹30 Delivery Charge
# Order amount 100–299 → ₹50 Delivery Charge
# Below 100 → Order not allowed
amount = int(input("Enter the amount: "))
if amount >= 500:
    print("Free Delivery")
elif 300 <= amount <= 499:
    print("30rs delivery charge")
elif 100 <= amount <= 299:
    print("50rs delivery charge")
elif amount < 100:
    print("Order not allowed")