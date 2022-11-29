# A dictionary is a collection which is unordered and changable(mutable) and indexed
# in python dictionaries are written with curly brackets, and they have keys and values.
# Example:-
# product1: 100
# product2: 200
# product3: 100   # kaeys should be unique but values can be duplicated

# creating a dictionary

# mydic={100:"Riya",101:"pavan",102:"sameer",103:"raghav",104:"Nitin",105:"priya",106:"usman"}
# print(mydic)

# access the items from the dictionary
mydic={
    100:"Riya",
    101:"pavan",
    102:"sameer",   # we can also write in this type not required to write in single line
    103:"raghav",
    104:"Nitin",
    105:"priya",
    106:"usman"
}
print(mydic[103])   # raghav  # here we can get the value using the key

# access using get ()
# mydic={100:"Riya",101:"pavan",102:"sameer",103:"raghav",104:"Nitin",105:"priya",106:"usman"}
# var=mydic.get(104)
# print(var)  # Nitin

# change value in the dictionary
