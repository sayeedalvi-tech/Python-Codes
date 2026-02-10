# 1. Cinema Ticket Counter
# A cinema allows entry only if:
# Age ≥ 18
# Show time is before 11 PM
# Display:
# "Ticket Confirmed"
# "Underage"
# "Show Closed"

print("Cinema Ticket Counter🎥")
age=int(input("Enter Your Age:"))
if age >= 18:
    print(f"Age is {age}")
    time=int(input("Enter show time:"))
    if time > 11:
        print(f"Show time is {time}")
        print("Tickets are confirmed")
    else:
        print("Slow Closed") 
else:
    print("You are Underage")

 #2.Online Exam Login
# A student can attend the exam if:
# Username is "student"
# Password is "exam2025"
# Login time is ≤ 10 AM
# Print proper message for each failure.

print("Online Exam Login📖")
user=input("Enter Username:")
passw=input("Enter Password:")
if user == "student" and passw=="exam2025":
    print("Login Succesful")
    time=int(input("Enter Time:"))
    if time <= 10:
        print(f"Time is {time}")
        print("Exam Started")
    else:
        print("Time has Exceeded")
        print("Exam Cannot be started now")
elif user=="student" and passw!="exam2025":
    print("Invalid Password")
elif user != "student" and passw=="exam2025":
    print("Invalid Username")
else:
    print("Invalid Credentials")

#3.    Online Food Delivery
# Order is accepted if:
# Restaurant is open ("yes")
# Order amount ≥ 200
# Delivery distance ≤ 8 km
# Print exact reason if rejected.

print("Online Food Delivery😋")
res=input("Restaurant is open?:")
if res=="yes":
    print("Restaurant is Open.")
    amo=int(input("Enter Amount:"))
    if amo >=200:
        print(f"Order Amount is {amo}")
        dis=int(input("Enter Distance:"))
        if dis <= 8:
            print("Restaurant is Open.")
            print(f"Order Amount is {amo}")
            print(f"Distance is {dis}")
            print("Order Accepted!")
        else:
            print("Order Cancelled as distance is more than 8km")
    else:
        print(f"Order Cancelled as amount is below 200")
else:
    print("Restaurant is closed.")
