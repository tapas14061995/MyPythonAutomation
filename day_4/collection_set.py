# creating a set
# set is a collection which is unordered and unindexed. In python sets are written with curly brackets
# myset={"apple","orange","coconut","cherry","egg"}
# print(myset)  # elements change their position everytime

# accessing the elements using loop

# myset={"apple","orange","coconut","cherry","egg"}
# for i in myset:
#     print(i)

# finding an element from the list

# myset={"apple","orange","coconut","cherry","egg"}
# print("cherry" in myset)  #True  # always returns True or false
# print("curry" in myset)  #False

# adding items to the set
# add():- adds single item    update():- adds multiple items

# myset={"apple","orange","coconut","cherry","egg"}
# myset.add("drinks")
# print(myset)

# myset={"apple","orange","coconut","cherry","egg"}
# myset.update(["guava","lichi"])   # we have to write in square brackets it is basically a list
# print(myset)

# Removing item from the list :--   remove ()   discard()
# myset={"apple","orange","coconut","cherry","egg"}
# myset.remove("orange")
# print(myset)
# myset.remove("papaya")    # returns keyerror

# myset={"apple","orange","coconut","cherry","egg"}
# myset.discard("orange")
# print(myset)
# myset.discard("papaya")   # returns no error

# clear all items from the set

# myset={"apple","orange","coconut","cherry","egg"}
# myset.clear()
# print(myset)   # returns set() which is a empty set. still the variable is present but the values got clear

# myset={"apple","orange","coconut","cherry","egg"}
# del myset
# print(myset)  # delete the values and also the variable

#joining of two sets   union()

# myset={"apple","orange","coconut","cherry","egg"}
# myset2={1,2,3,4,5}
# myset3=myset.union(myset2)
# print(myset3)  # order will not maintained in set

# another way of joining two sets using update()

# myset={"apple","orange","coconut","cherry","egg"}
# myset2={1,2,3,4,5}
# myset.update(myset2)
# print(myset)




