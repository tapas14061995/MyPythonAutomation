# create a string variable
# differrent ways tocreate a string variable
# name="Hello"
# name='Hello'
# name=str("Hello")
# name=str('Hello')
# creating empty string
# s=""
# s=''
# s=str()
# mutable: we cannot change the value of the variable
# immutable: can change the value of the variable
# string is immutable

# str1="Tapas"
# print(id(str1)) #2302683396400 # id of the variable str1
# str1=str1+"come here"
# print(id(str)) #140715897427056 # id of the variable changed
# if the value is changed after update then is immutable

# + and * operator in string

# str2="Hello"
# print(str2+"python")
# str3="Hello "
# print(str3*3) # * operator is used to print the string multiple times # (str*10 will print the string 10 times)

# string slicing

# ex="daughter"
# print(ex[1:4])   # aug
# print(ex[:5])  #daugh
# print(ex[2:])  #ughter
# print(ex[1:-1])  #aughte  last one char got removed
# print(ex[1:-2])  #aught  last two char got removed

# # example ord() and chr()
# print(ord('A'))  #65   # returns the ASCII code of the character
# print(ord('B'))  #66
# print(chr(65))  #A    # returns character represtented by ASCII number
# print(chr(90))  #Z

# min()  max()  len()
# print(min("school"))  #retuens c because in this string c is the minimum according to alphabatic order
# print(max("school"))  # returns s
# print(len("school"))  # returns length of the string which is 6

# example: in,  not in operator   returns True/False
# a="collection"
# print("lect" in a)  #returns True
# print("colti" in a)  #returns False

# print("lect" not in a) # returns False    # not in operator in opposite of in operator
# print("colti" not in a)# returns True

# string comparision: we can use relational operators ==,<=,>=,<,>,!=
# print("Tapas" == "Chiku")  #False
# print("Tapas" >= "chiku")  #False
# print("apple" <= "ball")  #True
# print("abc" > " ")  #True
# print("cat"!= "bat") #True

# Testing string :true/False

# s="welcome"
# print(s.isalnum())  #false
# print(s.isalpha()) #True
# t="123"
# print(t.isdigit())  # True #if a string contains only digits
# print("WELCOME".isupper())  # True if the string contains all upper cases
# print("welcome".islower())  #True
# print("That boy".isidentifier()) # False #if the string contains reserved keywords
# print(" ".isspace())  #if the string contains space

#searching for substrings
# s="welcome to python"
# print(s.endswith("thon"))  #True
# print(s.startswith("wel"))  #True
# print(s.find("come"))  #3  returns the index for come
# print(s.find("become"))  # returns -1 as this string is not there
# print(s.count("t"))  # returns 2 as it counts the number of occurances of that substring

#converting string
# x= "my name is chiku"
# print(x.capitalize()) # capitalize the first letter of the string  # My name is chiku
# print(x.upper())  # convert the string to upper case # MY NAME IS CHIKU
# print(x.lower())  # convert the string to lower case # my name is chiku
# print(x.title()) # coverts first letter of all words of the string to upper case # My Name Is Chiku
# print(x.swapcase()) # converts all upper case to lower case and vice versa #MY NAME IS CHIKU
# print(x.replace("chiku","Tapas")) # replaces in all occurances

#reverse a string
#method 1

y="contamination"
rev_str=""
for i in y:
    rev_str=i+rev_str
print("my reversed string is:",rev_str)

# method 2

# z="school"
# rev_str=z[::-1]
# print("my reverse string is :",rev_str)


