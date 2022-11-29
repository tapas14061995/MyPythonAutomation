# Tuple is a collection which is ordered and changable
# always written in round brackets
# it is immutable

# creating a tuple variable
# mytuple=("rice","sugar","curry")
# print(mytuple)

# accessing the items of the tuple
# mytuple=("rice","sugar","chicken")
# print(mytuple[2])   #chiken

# printing the range of tuple
# mytuple=("rice","sugar","chicken","curry","fish")
# print(mytuple[1:4])  #sugar, chicken, curry
# print(mytuple[-3:-1])  #chicken, curry

# changing of iems in tuple
# by default tuple doesnot allow you to change the value
# but we can change indirectly by modifying to list and again to tuple
# tuple ---> list(modify)  ---->list

mytuple=("bottle","coin","mouse")
mylist=list(mytuple)
mylist[1]="pen"
mytuple=tuple(mylist)
print(mytuple)    # bottle, pen, mouse

# below things are not possible in tuple
# (1)--we can not change existing value
# (2)--we cannot append new line
# (3)--we cannot insert new line
# (4)--we cannot remove a line
