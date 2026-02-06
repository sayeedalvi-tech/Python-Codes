#24. wap to Check whether string length is greater than 5
a=eval(input("enter string: "))
if len(a)>5:
    print("Yes")
else:
    print("no")

#24. wap to Check whether number is divisible by both 4 and 6\
a=int(input("Enter Number: "))
if a%4==0 and a%6==0:
    print("Yes")
else:
    print("NO")

if (a//4)*4==a and (a//6)*6==a:
    print("yes")
else:
    print("no")

#25. wap to Check whether number ends with zero
a=int(input("Enter Number: "))
if a%10==0:
    print("Ends with zero")
else:
    print("no")

#26. wap to Check whether a number is between 50 and 100
a=int(input("Enter Number: "))
if 50>=a>=100:
    print("Between 50 and 100")
else:
    print("Not between")

#27. wap to Check whether string length is divisible by 3 or not
a=eval(input("enter string: "))
if len(a)%3==0:
    print("Length divisible by 3")
else:
    print("NOt divisible")

#28. wap to Check whether number has exactly two digits
a=int(input("Enter Number: "))
b=str(a)
if len(b)==2:
    print("Two digit number")
else:
    print("not 2 digit")

#29. wap to Check whether a number ends with an even digit
a=int(input("Enter Number: "))
if (a%10)%2==0:
    print("ends with even number")
else:
    print("doesnot ends with even number")

#30. wap to Check whether a number is greater than its reverse
a=int(input("Enter Number: "))
b=str(a)
print(b[::-1])
if a >  int(b[::-1]):
    print("original is greater")
else:
    print("reverse is greater")

#31. wap to Check whether a number is divisible by its first digit
a=int(input("Enter Number: "))
b=str(a)
if a%int(b[0])==0:
    print("divisible by 1st number")
else:
    print("no")

#32. Check whether a number becomes palindrome after adding 1
a=int(input("Enter Number: "))
b=str(a+1)
print(f"b={a+1}")
if int(b) == int(b[::-1]):
    print("Yes it is palindrome")
else:
    print("no")

#33. check whether the square of a number ends with same digit as the number
a=int(input("Enter Number: "))
b=a**2
print(b)
if a%10 == b%10:
    print("Square and original ends with same digit")
else:
    print("no")

#34. Check whether the ASCII value of a character is even or odd
a=eval(input("Enter Character:"))
if ord(a)%2==0:
    print(ord(a))
    print("Even ASCII value")
else:
    print(ord(a))
    print("Odd ASCII value")