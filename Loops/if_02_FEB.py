# #20. WAP to check last numeber is even or odd
a=int(input("Enter number:"))
last_num = a%10
if last_num % 2==0:
    print(f"{a} is even")

if last_num % 2!=0:
    print(f"{a} is odd")

#21. WAp to check if given number is 3 digit number
a=int(input("Enter number:"))
if 100 <= a <= 999:
    print(f"{a} is 3 digit number")

#22. WAP to check if given number is 4 digit number
a=int(input("Enter number:"))
if 1000 <= a <= 9999:
    print(f"{a} is 4 digit number")

#23. WAp to check the given string starts with vowel
a=eval(input("Enter string:"))
if a[0] in "AEIOUaeiou":
    print(f"{a} starts with vowels")

#24. WAP to check if given string ends with consonant
a=eval(input("Enter string:"))
if a[-1] not in "AEIOUaeiou":
    print(f"{a} ends with vowels")

#25. Wap to check if given string has even number of characrter
a=eval(input("Enter string:"))
if len(a)%2==0:
    print(f"{a} has even length")

#26. Wap to check if given string has odd number of characrter
a=eval(input("Enter string:"))
if len(a)%2!=0:
    print(f"{a} has even length")

#27. WAp to chevk if the list first elemnet is even
a=eval(input("Enter list:"))
if a[0]%2==0:
    print(f"{a[0]} is even")

#27. WAp to chevk if the list first elemnet is odd
a=eval(input("Enter list:"))
if a[0]%2!=0:
    print(f"{a[0]} is odd")

#28. WAP to check the sum of 1st and last number is even
a=eval(input("Enter list:"))
b=a[0]+a[-1]
if b%2==0:
    print(f"{b} is even")

#29. WAP to check the sum of 1st and last number is odd
a=eval(input("Enter list:"))
b=a[0]+a[-1]
if b%2!=0:
    print(f"{b} is odd")

#30. WAP to check word is anagram(using one word to make another wword by shuffling)
a=eval(input("Enter string:"))   #silent
b=eval(input("Enter string:"))   #listen
if sorted(a) == sorted(b):
    print(f"{a} and {b} are anagram")

#31. WaP to check given number is postive
a=int(input("Enter Number:"))
if a > 0:
    print(f"{a} is positive")

#32. WaP to check given number is negative
a=int(input("Enter number:"))
if a < 0:
    print(f"{a} is negative")

#33. WaP to check given number is zero
a=int(input("Enter number:"))
if a == 0:
    print(f"{a} is zero")

#34. WaP to check given number is divisible by 5
a=int(input("Enter number:"))
if a%5==0:
    print(f"{a} is divisible by 5")

#35. WaP to check if 88 is less than 100
if 88<100:
    print("Yes it is less")

#36. WAP if string is lower case
a=eval(input("Enter String:"))
if a.islower():
    print(f"{a} is lower case")

#37. WAP if string is uppercase
a=eval(input("Enter String:"))
if a.isupper():
    print(f"{a} is uppercase")

#38. WAP to check if string contains space
a=eval(input("Enter String:"))
if ' ' in a:
    print(f"{a} contains space")

#39. WAP to check if string starts with capital letter
a=eval(input("Enter String:"))
if a[0].isupper:
    print("starts with upper case")

#40. Wap to checkk if string contains only alphabets
a=eval(input("Enter String:"))
if a.isaplha():
    print("String contains only alphabet")

#41. WAP to check if string contains only digit
a=eval(input("Enter String:"))
if a.isdigit():
    print("String Contains only digits")

#42. WaP to check if string ends with period ('.')
a=eval(input("Enter String:"))
if a.endswith('.'):
    print("String Ends with '.' ")

#43. WaP to check if 1st and last character are same
a=eval(input("Enter String:"))
if a[0]==a[-1]:
    print("Starts and end with same character")

#44. WAP to check if ASCII values is greater than 100.
a=eval(input("Enter Character:"))
print(ord(a))
if ord(a) > 100:
    print(f"ASCii Value of {a} is greater than 100")

#45. WaP to check if 5 exsist in list
a=eval(input("Enter List:"))
if 5 in a:
    print("5 is present in list")

#46. WaP to check if 1st and 2nd element are same
a=eval(input("Enter List:"))
if a[0]==a[1]:
    print("Same Elements")

#47. WaP to check if sum of list is greater than 100
a=eval(input("Enter List:"))
print(sum(a))
if sum(a) > 100:
    print("Sum Greater Than 100")

#48. WaP to check file name ends with .txt
a=eval(input("Enter String:"))
if a.endswith('.txt'):
    print("Name Ends with '.txt'")

#49. WaP to check if number is divisible by 3 and 7 
a=int(input("Enter Number:"))
if a%3==0 and a%7==0:
    print(f"{a} divisible by both 3 and 7")
    
#50. WAP to check if it is a 16-digit credit card number and contains only digits
a=eval(input("Enter cc number:"))
if len(a)==16 and a.isdigit():
    print("Yes its a cc number")

#51. WAP to check if student scored 70 then print good luck
a=int(input("Enter Number:"))
if a == 70:
    print("Good Luck")