# 01 . wap to check among 3 numbers which number is greater
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if x > y and x > z:
    print(f"{x} is greater than {y} and {z}")
elif y > x and y > z:
    print(f"{y} is greater than {x} and {z}")
else:
    print(f"{z} is greater than {x} and {y}")


# 02 . wap to check among 3 numbers which number is smaller
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if x < y and x < z:
    print(f"{x} is smaller than {y} and {z}")
elif y < x and y < z:
    print(f"{y} is smaller than {x} and {z}")
else:
    print(f"{z} is smaller than {x} and {y}")


# 03 . wap to develop a simple calculator
x = int(input("Enter the number:"))
y = int(input("Enter the number:"))
operator = input("Enter the operator:")
if operator == "+":
    print("Addition is",x + y)
elif operator == "-":
    print("Substraction is",x - y)
elif operator == "*":
    print("Multiplication is",x * y)
elif operator == "/":
    print("Division is",x / y)
elif operator == "%":
    print("Modulus is",x % y)
elif operator == "//":
    print("Floor Division is",x // y)
elif operator == "**":
    print("Exponent is",x ** y)
else:
    print("Invalid operator")


# 04 . wap to print day names if 1="Monday" and so on
n = int(input("Enter any number:"))
if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n == 7:
    print("Sunday")
else:
    print("Invalid Number")


# 05 . wap to check whether string starts with uppercase/lowercase/digit/special character
x = input("Enter any String:")
if ord("A") <= ord(x[0]) <= ord("Z"):
    print("String starts with uppercase")
elif ord("a") <= ord(x[0]) <= ord("z"):
    print("String starts with lowercase")
elif ord("0") <= ord(x[0]) <= ord("9"):
    print("String starts with digit")
else:
    print("String starts with special character")


# 06 . wap to take marks of 5 sub,calculate the average if average is b/w 90-100 print distinction
# if 75-89 print first class and
# if it is b/w 60-74 print second class
# if 50-59 print third class
# below 50 print fail
sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))
sub4 = int(input("Enter fourth subject marks: "))
sub5 = int(input("Enter fifth subject marks: "))
avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5
print("Average is: ", avg)
if 90 <= avg <= 100:
    print("Distinction")
elif 75 <= avg <= 89:
    print("First Class")
elif 60 <= avg <= 74:
    print("Second Class")
elif 50 <= avg <= 59:
    print("Third Class")
else:
    print("Failed...🤣")


# 07 . wap to check if it is child marriage(0-17) or
# Legal marriage(=18)
# Arrange marriage(18-30)
# Illegal marriage(30-35)
# Go to hell(35-40)
age = int(input("Enter the age: "))
if 0 <= age < 18:
    print("Child Marriage")
elif age == 18:
    print("Legal Marriage")
elif 18 < age <= 30:
    print("Arrange Marriage")
elif 30 < age <=35:
    print("Illegal Marriage")
elif 35 < age <= 40:
    print("Go to hell.....☠️☠️")


# 08 . wap to check a age belongs to category
# 0-17 child and 18 to 30 adult
# 31 to 60 men,61 to 100 senior citizen else invalid age
age = int(input("Enter the age: "))
if 0 <= age <= 17:
    print("Child")
elif 18 <= age <= 30:
    print("Adult")
elif 31 <= age <= 60:
    print("Men")
elif 61 <= age <=100:
    print("Senior Citizen")
else:
    print("Invalid Age")


# 09 . wap to check a data is a sequence/iterable/individual data type
# using isinstance
data =eval(input("Enter any data:"))
if isinstance(data,(str,tuple,list)):
    print("Sequence Data type")
elif isinstance(data,(int,float,complex,bool)):
    print("Individual Data type")
elif isinstance(data,(set,dict)):
    print("Iterable")

#using type
data =eval(input("Enter any data:"))
if type(data) in (str,tuple,list):
    print("Sequence Data type")
elif type(data) in (int,float,complex,bool):
    print("Individual Data type")
elif type(data) in (set,dict):
    print("Iterable")





