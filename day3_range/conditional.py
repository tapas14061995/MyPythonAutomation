# control statements
# (1) conditional statements: # if  if...else  elif
# (2) Looping statements: # while for
# (3) jumping statements: # break  continue
#(1) conditional statements: suppose i want to print if a person is eligible for vote or not
#age>=18
age=16
if age>=18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")
#example 2
if True:
    print("it is true")
else:
    print("it is false")
#example 3
if 1:
    print("one")
else:
    print("not one")
#example 3
#we have to find if a number is even or odd
num=20
if num%2==0:
    print("given number is even")
else:
    print("given number is odd")
#example 4
#if else in single line (ternary operator)
number=30
print("even number") if number%2==0 else print("odd number")
#example 6
#multiple statements in single line
b=25
{print("Hello"),print("python")} if b>=20 else {print("Hi"),print("Java")}
#example 7
#multiple conditions using elif
weekno=6
if weekno==1:
    print("sunday")
elif weekno==2:
    print("monday")
elif weekno==3:
    print("tuesday")
elif weekno==4:
    print("wednesday")
elif weekno==5:
    print("thrusday")
elif weekno==6:
    print("friday")
elif weekno==7:
    print("saturday")
else:
    print("invalid week number")
