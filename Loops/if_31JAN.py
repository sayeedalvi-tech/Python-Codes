
#1. Wap to check the given number is even
a=int(input("Enter Number:"))
if a%2==0:
    print(f"{a} is even")

#2.  Wap to check the given number is even without mod operator
a=int(input("Enter Number:"))
if (a//2)*2==a:
    print(f"{a} is even")

#3.  Wap to check the given number is odd
a=int(input("Enter Number:"))
if a%2!=0:
    print(f"{a} is odd")

#4. Wap to check the given number is odd/even using & operator(logical)
a=int(input("Enter Number:"))
if (a&1)==1:
    print(print(f"{a} is odd"))

if (a&1)==0:
    print(print(f"{a} is even"))

#5. Another way of even
a=int(input("Enter Number:"))
if a==(a//2)+(a//2):
    print(f"{a} is even")

#6. WAp to check if given string is in upper case
a=eval(input("Enter String:"))
if a.isupper():
    print(f"{a} is in upper case")

#7. Wap to check string is lower case
a=eval(input("Enter String:"))
if a.islower():
    print(f"{a} is in lower case")

#8. wap to check the charter is upper or not withot using string methods
a='A'
if ord('A') <= ord(a) <= ord('Z'):
    print(f"{a} is upper case")

#9. wap to check the charter is lower or not withot using string methods
a='m'
if ord('a') <= ord(a) <= ord('z'):
    print(f"{a} is lowercase")

#10. wap to check if given charater is digit or not
a=9
if a.isdigit():
    print(f"{a} is Digit")

if ord('1') <= ord(a) <= ord('9'):
    print(f"{a} is Digit")
