#52. WAP to check if a person is eligible to vote
a=eval(input("Enter age:"))
if a>=18:
    print("Eligible for voting")

#53. WAP to display "python coding" if number is greater than 1 and less than 5
a=int(input("Enter number:"))
if 1<a<5:
    print("Python Coding")

#54. WAP to checek whether a number is between 45 and 200 and divisible by 4 and 5
a=int(input("Enter number:"))
if (45<a<200) and (a%4==0 and a%5==0):
    print("Yes")
    print(chr(a))

#55. WAP to check if char is in uppercase. if yes convert to lover case and store in dict as key as asciii as value
a=eval(input("Enter char:"))
dic={}
if a.isupper():
    b=a.lower()
    dic[b]=ord(b)
    print(dic)

#56. WAP to check if char is a alphabet . if yes store in dict as key as asciii as value
a=eval(input("Enter char:"))
dic={}
if a.isalpha():
    dic[a]=ord(a)
    print(dic)

#57. WAP to check if the given chract is specail character
a=eval(input("Enter char:"))
if a.isalnum()==False:
    print(f"{a} is a Special Character")

if not ((ord("A") <= ord(a)<=ord("Z")) or (ord("a") <= ord(a)<=ord("z")) or (ord("0") <= ord(a)<=ord("9"))):
    print(f"{a} is a Special Character")


#58. WAP to check if number is perfect square
a=int(input("Enter Number:"))
b=int(a**0.5)
if b*b==a:
    print("Perfect Square root")

#59. WAP to see if tuple has more than 3 elements
a=eval(input("Enter Tuple:"))
if len(a) > 3:
    print("More than 3 elements")

#60. CHeck Success login
username=eval(input("ENter USername:"))
password=eval(input("ENter password:"))
if username=="Python" and password=="Master":
    print("Success")

#61. Check if Traffic signal action if it is red then stop
a=eval(input("Enter Action:"))
if a=="red":
    print("Stop")