#problem 1: check the given number is positive or negative
number=-60
if number >= 0:
    print("given number is positive")
else:
    print("given number is negative")
#problem 2: check largest of two number
num1=8
num2=7
if num1>num2:
    print("num1 is largest")
else:
    print("num2 is largest")
#method 2
print("num1 is largest") if num1>num2 else print("num2 is largest")
# problem 3: check largest of three number
a=20
b=32
c=44
if (a>b) and (a>c):
    print("a is the largest number")
elif (b>a) and (b>c):
    print("b is the largest number")
else:
    print("c is the largest number")
#problem 4: print week number if you provide week name as input
weekname=input("Enter week name ")
if weekname=='sunday':
    print("week number 1")
elif weekname=='monday':
    print("week number 2")
elif weekname=='tuesday':
    print("week number 3")
elif weekname=='wednesday':
    print("week number 4")
elif weekname=='thrusday':
    print("week number 5")
elif weekname=='friday':
    print("week number 6")
elif weekname=='saturday':
    print("week number 7")
else:
    print("invalid input")
