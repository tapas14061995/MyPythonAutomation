# list is a collecton which is ordered and changable hence it is mutable

# mylist1=["apple","cherry","ball"]
# mylist2=[1,2,3,4,5,6]
# mylist3=["jackets",3,10.5,None,True]

# accessing items from list

# print(mylist1[0])  #apple
# print(mylist3[2])  #10.5
# print(mylist3[-1])  #True

# Range of indexes

# print(mylist3[0:4])   # ['jackets', 3, 10.5, None]
# print(mylist3[-4:-1])  #[3, 10.5, None]

# changing of items in list

# mylist=["apple","banana","orange","kiwi"]
# print(mylist)
# mylist[2]="flower"
# print(mylist)   # ['apple', 'banana', 'flower', kiwi]

# Read the list items using --> loop statements

# mylist4=["apple","banana","orange"]
# for i in mylist4:
#     print(i)

#check item is present in the list or not

# mylist5=["ball","chocolate","drinks","food"]
# if "food" in mylist5:
#     print("yes..it is present")
# else:
#     print("No..it is not there")    # yes..it is present

# list length (counting of total number of items in the list)

# print(len(mylist5))   # 4

# adding new item to the list   append(),   insert()

# mylist6=["ball","chocolate","drinks","food"]
# mylist6.append("sugar")
# print(mylist6)  # adds item to the end of the list

# if we want to add item in the middle of the list then we use insert ()

# mylist7=["ball","chocolate","drinks","food"]
# mylist7.insert(2,"rice")
# print(mylist7)   # adds item to the index 2

# removing item from list using  pop()

# mylist=["ball","chocolate","drinks","food"]
# mylist.pop(3)  # here we specify index not value
# print(mylist)  # removes "food"

# #removing item using del keyword
# mylist=["ball","chocolate","drinks","food"]
# del mylist[3]  # here del command removes single item based on index
# print(mylist)

# clear all items of the list clear ()
# mylist=["ball","chocolate","drinks","food"]
# mylist.clear()   #clears all items of the list  but list variable will be available
# print(mylist)  #returns []

# copy list to another list

# mylist=["ball","chocolate","drinks","food"]
# mylist2=list(mylist)      # using list()
# print(mylist2)

# using copy()
# mylist=["ball","chocolate","drinks","food"]
# mylist2=mylist.copy()
# print(mylist2)

# joining of two lists or combining of lists
# list1=["snake","ladder","dice"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# using loop statement

# list1=["snake","ladder","dice"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)

# method 3  for joining two lists using extend()

# list3=["snake","ladder","dice"]
# list4=["ravi","nitin","arvind"]
# list3.extend(list4)
# print(list3)












