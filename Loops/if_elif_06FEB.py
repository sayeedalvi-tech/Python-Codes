#1. WaP to check if the given number is postive or negative or neutral
a=int(input("Enter Number:"))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Neutral")

#2. Wap to check if given character is upper case or lower case or digit
a=eval(input("Enter String"))
if a.isupper():
    print("Upper case")
elif a.islower():
    print("Lower Case")
elif a.isdigit():
    print("Digit")

if ord('A') >= ord(a) >= ord('Z'):
    print("Upper case")
elif ord('a') >= ord(a) >= ord('z'):
    print("Lower Case")
elif ord('0') >= ord(a) >= ord('9'):
    print("Digit")

#3. WAP to check the given data type is string and return its length else given data type is list pop the element else
# if tuple then reverse the tuple else invalid dattype
a=eval(input("Enter data:"))
if type(a)==str:
    print(len(a))
elif type(a)==list:
    print(a.pop())
    print(a)
elif type(a)==tuple:
    print(tuple(sorted(a,reverse=True)))
else:
    print("Invalid Datatype")


if isinstance(a,str):
    print(len(a))
elif isinstance(a,list):
    print(a.pop())
    print(a)
elif isinstance(a,tuple):
    print(tuple(sorted(a,reverse=True)))
else:
    print("Invalid Datatype")